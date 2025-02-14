import json
from functions.getJsonContent import getJsonContent

def exportTableData(table_name: str, file_path: str):
    """
    Exports the table data to a JSON file at file_path.
    """
    data = getJsonContent(table_name)
    if not isinstance(data, list):
        return "Table not found or invalid data"
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        return f"Export failed: {e}"
    return "Data exported successfully"
