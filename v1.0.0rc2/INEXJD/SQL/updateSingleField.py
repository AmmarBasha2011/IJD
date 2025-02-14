from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def updateSingleField(table_name: str, index: int, field: str, new_value):
    """
    Updates a single field in a record at the specified index.
    """
    data = getJsonContent(table_name)
    if index < 0 or index >= len(data):
        return "Invalid index"
    if field not in data[index]:
        return "Field not found"
    data[index][field] = new_value
    writeJsonContent(data, table_name)
    return "Field updated successfully"
