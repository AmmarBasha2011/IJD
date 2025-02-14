from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def mergeTablesData(target_table: str, source_table: str):
    """
    Merges data from the source table into the target table.
    """
    target_data = getJsonContent(target_table)
    source_data = getJsonContent(source_table)
    if not isinstance(target_data, list) or not isinstance(source_data, list):
        return "Invalid table data"
    merged_data = target_data + source_data
    writeJsonContent(merged_data, target_table)
    return "Tables merged successfully"
