from ..functions.getJsonContent import getJsonContent


def get_distinct(table_name, field_name):
    """
    Get distinct values of a field from a table.
    
    Args:
        table_name (str): Target table
        field_name (str): Field to get distinct values from
    
    Returns:
        list: Unique values for the field
    """
    table_data = getJsonContent(table_name)
    unique_values = []
    seen = set()
    
    for record in table_data:
        value = record.get(field_name)
        # Convert unhashable types (like lists/dicts) to tuples for comparison
        value_key = tuple(value) if isinstance(value, (list, dict)) else value
        
        if value_key not in seen:
            seen.add(value_key)
            unique_values.append(value)
    
    return unique_values
