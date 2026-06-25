import os
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent

_indexes = {}
_indexes_file = "indexes"


def _load_indexes():
    global _indexes
    try:
        data = getJsonContent(_indexes_file)
        _indexes = data if isinstance(data, dict) else {}
    except FileNotFoundError:
        _indexes = {}


def _save_indexes():
    writeJsonContent(_indexes, _indexes_file)


def create_index(table_name, field_name):
    """
    Create an index on a field for faster lookups.
    
    Args:
        table_name (str): Name of the table
        field_name (str): Field to index
    """
    _load_indexes()
    
    if table_name not in _indexes:
        _indexes[table_name] = {}
    
    if field_name in _indexes[table_name]:
        return "Index already exists"
    
    # Build the index
    table_data = getJsonContent(table_name)
    index = {}
    
    for idx, record in enumerate(table_data):
        value = record.get(field_name)
        if value not in index:
            index[value] = []
        index[value].append(idx)
    
    _indexes[table_name][field_name] = index
    _save_indexes()
    
    return "Index created successfully"


def drop_index(table_name, field_name):
    """
    Drop an existing index.
    
    Args:
        table_name (str): Name of the table
        field_name (str): Indexed field
    """
    _load_indexes()
    
    if table_name not in _indexes or field_name not in _indexes[table_name]:
        return "Index not found"
    
    del _indexes[table_name][field_name]
    if not _indexes[table_name]:
        del _indexes[table_name]
    _save_indexes()
    
    return "Index dropped successfully"


def search_with_index(table_name, field_name, value):
    """
    Search for records using an index.
    
    Args:
        table_name (str): Name of the table
        field_name (str): Field to search
        value: Value to look for
    
    Returns:
        list: Matching records or None if no index exists
    """
    _load_indexes()
    
    if (table_name not in _indexes or field_name not in _indexes[table_name]):
        return None
    
    index = _indexes[table_name][field_name]
    indices = index.get(value, [])
    table_data = getJsonContent(table_name)
    
    return [table_data[i] for i in indices]


def update_index(table_name, field_name, table_data=None):
    """
    Update the index after data changes.
    
    Args:
        table_name (str): Name of the table
        field_name (str): Indexed field
        table_data (list, optional): Current table data
    """
    _load_indexes()
    
    if (table_name not in _indexes or field_name not in _indexes[table_name]):
        return "Index not found"
    
    if table_data is None:
        table_data = getJsonContent(table_name)
    
    index = {}
    for idx, record in enumerate(table_data):
        value = record.get(field_name)
        if value not in index:
            index[value] = []
        index[value].append(idx)
    
    _indexes[table_name][field_name] = index
    _save_indexes()
    
    return "Index updated successfully"


def list_indexes(table_name=None):
    """
    List all indexes.
    
    Args:
        table_name (str, optional): List indexes for a specific table only
    """
    _load_indexes()
    
    if table_name is None:
        return _indexes
    return _indexes.get(table_name, {})
