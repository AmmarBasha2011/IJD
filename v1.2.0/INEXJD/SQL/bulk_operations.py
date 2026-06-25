from .getTableStructure import getTableStructure
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def bulk_insert(table_name, records):
    """
    Insert multiple records at once.
    
    Args:
        table_name (str): Target table
        records (list): List of record dictionaries
    
    Returns:
        str: Result message
    """
    table_structure = getTableStructure(table_name)
    if isinstance(table_structure, str):
        return "Table not found"
    
    for record in records:
        if set(record.keys()) != set(table_structure):
            return f"Record {record} has invalid fields"
    
    table_data = getJsonContent(table_name)
    table_data.extend(records)
    writeJsonContent(table_data, table_name)
    
    return f"Bulk inserted {len(records)} records successfully"


def bulk_update(table_name, condition, new_data):
    """
    Update all records matching a condition.
    
    Args:
        table_name (str): Target table
        condition (dict): Key-value pairs to match
        new_data (dict): Key-value pairs to update
    
    Returns:
        str: Result message
    """
    table_data = getJsonContent(table_name)
    updated_count = 0
    
    for record in table_data:
        match = True
        for k, v in condition.items():
            if record.get(k) != v:
                match = False
                break
        if match:
            record.update(new_data)
            updated_count += 1
    
    if updated_count > 0:
        writeJsonContent(table_data, table_name)
        return f"Bulk updated {updated_count} records successfully"
    return "No matching records found"


def bulk_delete(table_name, condition):
    """
    Delete all records matching a condition.
    
    Args:
        table_name (str): Target table
        condition (dict): Key-value pairs to match
    
    Returns:
        str: Result message
    """
    table_data = getJsonContent(table_name)
    new_data = []
    deleted_count = 0
    
    for record in table_data:
        match = True
        for k, v in condition.items():
            if record.get(k) != v:
                match = False
                break
        if not match:
            new_data.append(record)
        else:
            deleted_count += 1
    
    if deleted_count > 0:
        writeJsonContent(new_data, table_name)
        return f"Bulk deleted {deleted_count} records successfully"
    return "No matching records found"
