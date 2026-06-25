import os

def removeFile(file_name: str):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    file_path = os.path.join(json_dir, f'{file_name}.json')
    if os.path.exists(file_path):
        os.remove(file_path)
        return "File removed successfully"
    return "File not found"