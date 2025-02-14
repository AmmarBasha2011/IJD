from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent
import os

def renameTable(old_name: str, new_name: str):
    content = getJsonContent("tables")
    if old_name not in content["tables"]:
        return "Old table not found"
    if new_name in content["tables"]:
        return "New table name already exists"
    content["tables"][new_name] = content["tables"].pop(old_name)
    writeJsonContent(content, "tables")
    os.rename(f"{old_name}.json", f"{new_name}.json")
    return "Table renamed successfully"
