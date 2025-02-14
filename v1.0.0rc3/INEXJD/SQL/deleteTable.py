from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def deleteTable(table_name: str):
    # Get the json content
    content = getJsonContent("tables")

    if table_name not in content["tables"]:
        return "Table not found"
    
    del content["tables"][table_name]
    writeJsonContent(content, "tables")
    return "Table deleted successfully"