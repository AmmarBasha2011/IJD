from functions.getJsonContent import getJsonContent

def getRecordById(table_name: str, record_id):
    data = getJsonContent(table_name)
    for record in data:
        if record.get("id") == record_id:
            return record
    return "Record not found"
