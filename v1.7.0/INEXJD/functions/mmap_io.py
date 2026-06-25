import os
import mmap
import json


def read_mmap_json(file_path):
    """
    Read a JSON file using memory mapping for large files.
    
    Args:
        file_path (str): Path to JSON file
    
    Returns:
        dict/list: Parsed JSON data
    """
    with open(file_path, 'r') as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
            data = mm.read()
            return json.loads(data.decode('utf-8'))


def write_mmap_json(data, file_path):
    """
    Write JSON data using efficient file handling (for large files).
    
    Args:
        data: JSON-serializable data
        file_path (str): Path to write to
    """
    json_str = json.dumps(data, indent=4)
    with open(file_path, 'w') as f:
        f.write(json_str)
