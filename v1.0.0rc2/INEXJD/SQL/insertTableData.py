from SQL.getTableStructure import getTableStructure
from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def insertTableData(table_name: str, data: dict):
    # Get the table structure
    table_structure = getTableStructure(table_name)
    if isinstance(table_structure, str):
        return "Table not found"

    # Check if data keys match table structure
    if set(data.keys()) != set(table_structure):
        return "Data fields do not match table structure"

    # Get the json content
    content = getJsonContent(table_name)

    content.append(data)
    writeJsonContent(content, table_name)
    return "Data inserted successfully"