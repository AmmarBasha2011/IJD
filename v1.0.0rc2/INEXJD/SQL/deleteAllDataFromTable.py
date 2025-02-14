from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def deleteAllDataFromTable(table_name: str):
    # Get the json content
    content = getJsonContent(table_name)

    writeJsonContent({}, table_name)
    return "All data deleted from table successfully"