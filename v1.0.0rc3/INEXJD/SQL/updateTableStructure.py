from functions.getJsonContent import getJsonContent
from functions.removeFile import removeFile
from functions.writeJsonContent import writeJsonContent

def updateTableStructure(table_name: str, paramas: list):
    # Get the json content
    content = getJsonContent("tables")

    if table_name not in content["tables"]:
        return "Table not found"

    removeFile(table_name)
    content["tables"][table_name] = paramas
    writeJsonContent(content, "tables")
    writeJsonContent({}, table_name)
    return "Table updated successfully"