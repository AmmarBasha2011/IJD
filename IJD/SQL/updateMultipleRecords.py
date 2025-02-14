from functions.getJsonContent import getJsonContent
from functions.writeJsonContent import writeJsonContent

def updateMultipleRecords(table_name: str, condition: dict, new_data: dict):
    data = getJsonContent(table_name)
    updated = False
    for record in data:
        if all(record.get(k) == v for k, v in condition.items()):
            record.update(new_data)
            updated = True
    if updated:
        writeJsonContent(data, table_name)
        return "Records updated successfully"
    return "No matching records found"
