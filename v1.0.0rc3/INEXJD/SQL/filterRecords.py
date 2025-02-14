from functions.getJsonContent import getJsonContent

def filterRecords(table_name: str, condition: dict):
    """
    Filters records in a table that satisfy all key-value pairs in the condition.
    """
    data = getJsonContent(table_name)
    if not isinstance(data, list):
        return "Table not found or invalid data"
    filtered = [record for record in data if all(record.get(k) == v for k, v in condition.items())]
    return filtered
