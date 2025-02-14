from functions.getTableStructure import getTableStructure

def listTableFields(table_name: str):
    structure = getTableStructure(table_name)
    if isinstance(structure, list):
        return structure
    return "Table not found"
