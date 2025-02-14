from functions.getJsonContent import getJsonContent


def getTables():
    # Get the json content
    content = getJsonContent("tables")

    return content["tables"]