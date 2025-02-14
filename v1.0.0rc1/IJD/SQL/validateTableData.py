from functions.getJsonContent import getJsonContent
from functions.getTableStructure import getTableStructure

def validateTableData(table_name: str):
    data = getJsonContent(table_name)
    structure = getTableStructure(table_name)
    if not isinstance(structure, list):
        return "Table structure not found"
    for record in data:
        if set(record.keys()) != set(structure):
            return "Invalid record format detected"
    return "All records are valid"
