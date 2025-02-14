from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def createTable(table_name: str, paramas: list):
    # Get the json content
    content = getJsonContent("tables")

    if table_name in content["tables"]:
        return "Table already exists"
    
    content["tables"][table_name] = paramas
    writeJsonContent(content, "tables")
    writeJsonContent({}, table_name)

    return "Table created successfully"