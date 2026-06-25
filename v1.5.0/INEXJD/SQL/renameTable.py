from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent
import os

def renameTable(old_name: str, new_name: str):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    content = getJsonContent("tables")
    if old_name not in content["tables"]:
        return "Old table not found"
    if new_name in content["tables"]:
        return "New table name already exists"
    content["tables"][new_name] = content["tables"].pop(old_name)
    writeJsonContent(content, "tables")
    old_path = os.path.join(json_dir, f"{old_name}.json")
    new_path = os.path.join(json_dir, f"{new_name}.json")
    os.rename(old_path, new_path)
    return "Table renamed successfully"
