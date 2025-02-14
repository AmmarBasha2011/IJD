from functions.getJsonContent import getJsonContent


def getTableData(table_name: str):
    # Get the json content
    content = getJsonContent(table_name)

    return content