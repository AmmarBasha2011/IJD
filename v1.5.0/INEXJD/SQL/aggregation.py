from ..functions.getJsonContent import getJsonContent


def aggregate(table_name, agg_fields, group_by=None, having=None):
    """
    Perform aggregation with optional GROUP BY and HAVING.
    
    Args:
        table_name (str): Target table
        agg_fields (dict): {alias: ("function, field} (e.g. {"avg_age": ("AVG", "age")})
        group_by (str/list, optional): Field(s) to group by
        having (dict, optional): Condition to filter groups (same format as filter_where)
    
    Returns:
        list: Aggregated results
    """
    table_data = getJsonContent(table_name)
    aggregators = {
        "SUM": sum,
        "AVG": lambda x: sum(x)/len(x) if x else None,
        "COUNT": len,
        "MAX": max,
        "MIN": min
    }
    
    if group_by is None:
        result = {}
        for alias, (func_name, field) in agg_fields.items():
            values = [r[field] for r in table_data if r.get(field) is not None]
            result[alias] = aggregators[func_name](values)
        return [result]
    else:
        groups = {}
        for record in table_data:
            key = tuple(record.get(f) for f in (group_by if isinstance(group_by, list) else [group_by]))
            if key not in groups:
                groups[key] = []
            groups[key].append(record)
        
        group_results = []
        for group_key, records in groups.items():
            group_data = {}
            if isinstance(group_by, list):
                for i, f in enumerate(group_by):
                    group_data[f] = group_key[i]
            else:
                group_data[group_by] = group_key[0]
            for alias, (func_name, field) in agg_fields.items():
                values = [r.get(field) for r in records if r.get(field) is not None]
                group_data[alias] = aggregators[func_name](values)
            group_results.append(group_data)
        
        if having is not None:
            from .where_clause import filter_where
            # Wait, filter the groups with having: we'll need to adapt
            # Just implement simple having check
            def _check_having(rec, cond):
                if "AND" in cond: return all(_check_having(rec, c) for c in cond["AND"])
                if "OR" in cond: return any(_check_having(rec, c) for c in cond["OR"])
                field = cond.get("field")
                op = cond.get("operator")
                value = cond.get("value")
                field_val = rec.get(field)
                if op == "=": return field_val == value
                if op == ">": return field_val > value
                if op == "<": return field_val < value
                if op == ">=": return field_val >= value
                if op == "<=": return field_val <= value
                if op == "<>": return field_val != value
                return False
            group_results = [g for g in group_results if _check_having(g, having)]
        return group_results
