from functions.getJsonContent import getJsonContent

def countRecordsByCondition(table_name: str, condition: dict):
    data = getJsonContent(table_name)
    count = sum(1 for record in data if all(record.get(k) == v for k, v in condition.items()))
    return count
