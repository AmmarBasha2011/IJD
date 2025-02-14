import os

def removeFile(file_name: str):
    file_name = f"../Json/{file_name}.json"
    if os.path.exists(file_name):
        os.remove(file_name)
        return "File removed successfully"
    return "File not found"