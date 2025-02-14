from functions.getJsonContent import getJsonContent
from functions.removeFile import removeFile
from functions.writeJsonContent import writeJsonContent

def deleteAllTables():
    # Get the json content
    content = getJsonContent("tables")

    for table_name in content["tables"]:
        removeFile(table_name)
    
    removeFile("tables")
    writeJsonContent({}, "tables")
    return "All tables deleted successfully"