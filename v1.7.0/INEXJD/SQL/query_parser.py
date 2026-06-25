import re
from ..functions.getJsonContent import getJsonContent
from .where_clause import filter_where
from .pagination import paginate
from .orderby import sort_by_multiple
from .distinct import get_distinct


def parse_query(query):
    """
    Parse a simplified SQL-like query string.
    
    Supported syntax:
    - SELECT [* | field1, field2] FROM table [WHERE condition]
    - SELECT DISTINCT field FROM table
    - SELECT ... [ORDER BY field [ASC|DESC]]
    - SELECT ... [LIMIT n [OFFSET m]]
    
    Args:
        query (str): SQL-like query
        
    Returns:
        dict: Parsed query components
    """
    query = query.strip()
    result = {
        "type": None,
        "table": None,
        "fields": [],
        "where": None,
        "order_by": [],
        "limit": None,
        "offset": 0,
        "distinct": False
    }
    
    # SELECT
    select_match = re.match(r"SELECT\s+(DISTINCT\s+)?(.+?)\s+FROM\s+(\w+)", query, re.IGNORECASE)
    if select_match:
        result["type"] = "SELECT"
        if select_match.group(1):
            result["distinct"] = True
        result["fields"] = [f.strip() for f in select_match.group(2).split(",")]
        result["table"] = select_match.group(3)
        
        # WHERE
        where_match = re.search(r"WHERE\s+(.+?)(?:\s+(ORDER|LIMIT)\s+|$)", query, re.IGNORECASE)
        if where_match:
            where_str = where_match.group(1).strip()
            # Simple where for single condition
            cond_match = re.match(r"(\w+)\s*(=|>|<|>=|<=|!=|LIKE|IN)\s*([^;]+)", where_str, re.IGNORECASE)
            if cond_match:
                result["where"] = {
                    "field": cond_match.group(1),
                    "operator": cond_match.group(2),
                    "value": cond_match.group(3).strip()
                }
                # Try to parse value type
                val_str = result["where"]["value"]
                if val_str.startswith("'") and val_str.endswith("'"):
                    result["where"]["value"] = val_str[1:-1]
                elif val_str.lower() in ["true", "false"]:
                    result["where"]["value"] = val_str.lower() == "true"
                else:
                    try:
                        if "." in val_str:
                            result["where"]["value"] = float(val_str)
                        else:
                            result["where"]["value"] = int(val_str)
                    except ValueError:
                        pass
        
        # ORDER BY
        order_match = re.search(r"ORDER BY\s+(.+?)(?:\s+LIMIT|$)", query, re.IGNORECASE)
        if order_match:
            order_str = order_match.group(1).strip()
            for part in order_str.split(","):
                part = part.strip()
                parts = part.split()
                field = parts[0]
                reverse = len(parts) > 1 and parts[1].upper() == "DESC"
                result["order_by"].append({"field": field, "reverse": reverse})
        
        # LIMIT
        limit_match = re.search(r"LIMIT\s+(\d+)(?:\s+OFFSET\s+(\d+))?", query, re.IGNORECASE)
        if limit_match:
            result["limit"] = int(limit_match.group(1))
            if limit_match.group(2):
                result["offset"] = int(limit_match.group(2))
    else:
        raise ValueError("Unsupported query syntax")
    
    return result


def execute_query(query):
    """
    Execute a simplified SQL-like query.
    
    Args:
        query (str): SQL-like query
        
    Returns:
        list: Query results
    """
    parsed = parse_query(query)
    if parsed["type"] != "SELECT":
        raise ValueError("Only SELECT queries are supported right now")
    
    # Get table data
    data = getJsonContent(parsed["table"])
    
    # WHERE
    if parsed["where"]:
        where_dict = {
            "AND": [parsed["where"]]
        }
        data = filter_where(parsed["table"], where_dict)
    
    # DISTINCT
    if parsed["distinct"] and len(parsed["fields"]) == 1:
        data = get_distinct(parsed["table"], parsed["fields"][0])
    
    # ORDER BY
    if parsed["order_by"]:
        data = sort_by_multiple(parsed["table"], parsed["order_by"])
    
    # LIMIT & OFFSET
    if parsed["limit"]:
        data = paginate(parsed["table"], parsed["limit"], parsed["offset"])
    
    # Field projection
    if parsed["fields"] != ["*"] and not parsed["distinct"]:
        projected_data = []
        for row in data:
            proj_row = {}
            for f in parsed["fields"]:
                proj_row[f] = row.get(f)
            projected_data.append(proj_row)
        data = projected_data
    
    return data
