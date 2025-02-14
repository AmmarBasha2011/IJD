from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def sortTableData(table_name: str, key: str, reverse: bool = False):
    """
    Sorts the records in the table by the specified key.
    """
    data = getJsonContent(table_name)
    if not isinstance(data, list):
        return "Table not found or invalid data"
    try:
        sorted_data = sorted(data, key=lambda x: x.get(key, None), reverse=reverse)
    except Exception as e:
        return f"Error during sorting: {e}"
    writeJsonContent(sorted_data, table_name)
    return "Data sorted successfully"
