from functions.getJsonContent import getJsonContent

def getTableStructure(table_name: str):
    # Get the json content
    content = getJsonContent("tables")

    if table_name not in content["tables"]:
        return "Table not found"
    
    return content["tables"][table_name]