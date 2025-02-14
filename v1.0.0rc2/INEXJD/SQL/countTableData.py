from functions.getJsonContent import getJsonContent

def countTableData(table_name: str):
    """
    Returns the count of records in the table.
    """
    data = getJsonContent(table_name)
    if not isinstance(data, list):
        return "Table not found or invalid data"
    return len(data)
