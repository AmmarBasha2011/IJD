import json
from functions.writeJsonContent import writeJsonContent

def restoreTableData(table_name: str, backup_path: str):
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        writeJsonContent(data, table_name)
        return "Table restored successfully"
    except Exception as e:
        return f"Restore failed: {str(e)}"
