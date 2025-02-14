from SQL.getTableStructure import getTableStructure
from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def deleteTableData(table_name: str, index: int):
    # Get the table structure
    table_structure = getTableStructure(table_name)
    if isinstance(table_structure, str):
        return "Table not found"

    # Get the json content
    content = getJsonContent(table_name)

    del content[index]
    writeJsonContent(content, table_name)
    return "Data deleted successfully"