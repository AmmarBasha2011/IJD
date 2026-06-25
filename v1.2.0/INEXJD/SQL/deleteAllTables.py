from ..functions.getJsonContent import getJsonContent
from ..functions.removeFile import removeFile
from ..functions.writeJsonContent import writeJsonContent

def deleteAllTables():
    try:
        # Get the json content
        content = getJsonContent("tables")
        if "tables" in content:
            for table_name in content["tables"]:
                removeFile(table_name)
        removeFile("tables")
    except FileNotFoundError:
        pass
    writeJsonContent({"tables": {}}, "tables")
    return "All tables deleted successfully"