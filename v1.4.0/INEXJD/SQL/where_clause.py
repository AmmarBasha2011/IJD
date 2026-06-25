from ..functions.getJsonContent import getJsonContent


def _like_match(value, pattern):
    """
    Simple LIKE pattern matching (supports % as wildcard).
    """
    import re
    regex = pattern.replace('%', '.*')
    return re.fullmatch(regex, str(value)) is not None


def filter_where(table_name, conditions):
    """
    Filter table data using complex conditions.
    
    Args:
        table_name (str): Target table
        conditions (dict/list): Condition(s) to apply. Can be:
            - Single dict: {"field": "age", "operator": ">", "value": 30}
            - List with AND/OR: {"AND": [cond1, cond2]} or {"OR": [cond1, cond2]}
    
    Returns:
        list: Matching records
    """
    table_data = getJsonContent(table_name)
    
    def matches_condition(record, cond):
        if "AND" in cond:
            return all(matches_condition(record, c) for c in cond["AND"])
        if "OR" in cond:
            return any(matches_condition(record, c) for c in cond["OR"])
        
        field = cond.get("field")
        op = cond.get("operator")
        value = cond.get("value")
        field_val = record.get(field)
        
        if op == "=":
            return field_val == value
        elif op == "<>":
            return field_val != value
        elif op == ">":
            return field_val > value
        elif op == "<":
            return field_val < value
        elif op == ">=":
            return field_val >= value
        elif op == "<=":
            return field_val <= value
        elif op == "LIKE":
            return _like_match(field_val, value)
        elif op == "IN":
            return field_val in value
        elif op == "BETWEEN":
            return value[0] <= field_val <= value[1]
        return False
    
    return [r for r in table_data if matches_condition(r, conditions)]
