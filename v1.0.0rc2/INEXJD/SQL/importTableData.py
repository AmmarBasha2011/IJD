import json
from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def importTableData(table_name: str, file_path: str):
    """
    Imports data from a JSON file at file_path into the table.
    Appends the imported records to the existing table data.
    """
    try:
        with open(file_path, "r") as f:
            imported_data = json.load(f)
    except Exception as e:
        return f"Import failed: {e}"
    data = getJsonContent(table_name)
    if not isinstance(data, list):
        return "Table not found or invalid data"
    if not isinstance(imported_data, list):
        return "Imported file must contain a list of records"
    merged_data = data + imported_data
    writeJsonContent(merged_data, table_name)
    return "Data imported successfully"
