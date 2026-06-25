from ..functions.getJsonContent import getJsonContent


def sort_by_multiple(table_name, sort_keys):
    """
    Sort a table by multiple fields.
    
    Args:
        table_name (str): Target table
        sort_keys (list): List of dicts like [{"field": "name", "reverse": False}, ...]
    
    Returns:
        list: Sorted table data
    """
    table_data = getJsonContent(table_name)
    
    # Sort using tuple of keys (supports multiple fields)
    sorted_data = sorted(table_data, key=lambda x: tuple(
        (x.get(key["field"]) if not key.get("reverse") else -x.get(key["field"]) if isinstance(x.get(key["field"]), (int, float)) else x.get(key["field"))
        for key in sort_keys
    ))
    
    # Apply reverse for individual fields (since lambda key doesn't handle reverse per field perfectly)
    # Alternative approach: sort from last key to first
    for key in reversed(sort_keys):
        sorted_data.sort(key=lambda x: x.get(key["field"]), reverse=key.get("reverse", False))
    
    return sorted_data
