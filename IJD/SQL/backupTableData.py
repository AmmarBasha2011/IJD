import json
from functions.getJsonContent import getJsonContent

def backupTableData(table_name: str, backup_path: str):
    data = getJsonContent(table_name)
    try:
        with open(backup_path, 'w') as f:
            json.dump(data, f, indent=2)
        return "Table backup created successfully"
    except Exception as e:
        return f"Backup failed: {str(e)}"
