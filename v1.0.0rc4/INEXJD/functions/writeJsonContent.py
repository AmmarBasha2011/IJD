import json

def writeJsonContent(data, file_path):
    """
    Write JSON content to a file.
    
    Args:
        data: The data to be written as JSON
        file_path (str): The path to the file where JSON will be written
    """
    file_path = f"/Json/{file_path}.json"
    
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception as e:
        print(f"Error writing JSON file: {str(e)}")
        return False