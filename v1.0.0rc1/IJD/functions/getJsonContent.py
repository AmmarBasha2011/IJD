import json

def getJsonContent(file_name):
    try:
        # Read the file content
        with open(f'../Json/{file_name}.json', 'r') as file:
            file_content = file.read()
        
        # Try to parse JSON and verify it's a dict or list
        json_data = json.loads(file_content)
        if not isinstance(json_data, (dict, list)):
            raise ValueError("Content is not JSON data")
            
        # Return the JSON content
        return json_data
    except (json.JSONDecodeError, ValueError) as e:
        raise ValueError(f"Invalid JSON data: {str(e)}")