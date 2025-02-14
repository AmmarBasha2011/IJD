from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent
import copy

def duplicateTableData(table_name: str, index: int):
    """
    Duplicates the record at the specified index and appends it to the table.
    """
    data = getJsonContent(table_name)
    if index < 0 or index >= len(data):
        return "Invalid index"
    new_record = copy.deepcopy(data[index])
    data.append(new_record)
    writeJsonContent(data, table_name)
    return "Record duplicated successfully"
