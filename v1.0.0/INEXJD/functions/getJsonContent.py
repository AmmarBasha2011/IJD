import json
import os

def getJsonContent(file_name):
    try:
        # Get the directory of the current file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_dir = os.path.join(base_dir, "Json")
        file_path = os.path.join(json_dir, f'{file_name}.json')
        
        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()
        
        # Try to parse JSON and verify it's a dict or list
        json_data = json.loads(file_content)
        if not isinstance(json_data, (dict, list)):
            raise ValueError("Content is not JSON data")
            
        # Return the JSON content
        return json_data
    except (json.JSONDecodeError, ValueError) as e:
        raise ValueError(f"Invalid JSON data: {str(e)}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_name}.json not found in Json directory")