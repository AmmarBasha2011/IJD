from functions.getJsonContent import getJsonContent

def searchTableData(table_name: str, query: dict):
    """
    Searches for records in the table which match all key-value pairs in query.
    """
    data = getJsonContent(table_name)
    if not isinstance(data, list):
        return "Table not found or invalid data"
    result = [record for record in data if all(record.get(k) == v for k, v in query.items())]
    return result
