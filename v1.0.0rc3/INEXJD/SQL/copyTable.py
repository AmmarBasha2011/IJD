from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def copyTable(source: str, destination: str):
    content = getJsonContent("tables")
    if source not in content["tables"]:
        return "Source table not found"
    if destination in content["tables"]:
        return "Destination table already exists"
    content["tables"][destination] = content["tables"][source]
    writeJsonContent(content, "tables")
    data = getJsonContent(source)
    writeJsonContent(data, destination)
    return "Table copied successfully"
