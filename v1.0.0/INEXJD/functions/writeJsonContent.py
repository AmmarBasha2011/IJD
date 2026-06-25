import json
import os

def writeJsonContent(data, file_name):
    """
    Write JSON content to a file.
    
    Args:
        data: The data to be written as JSON
        file_name (str): The name of the file (without .json extension) where JSON will be written
    """
    # Get the directory of the current file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    # Ensure Json directory exists
    os.makedirs(json_dir, exist_ok=True)
    file_path = os.path.join(json_dir, f'{file_name}.json')
    
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception as e:
        print(f"Error writing JSON file: {str(e)}")
        return False