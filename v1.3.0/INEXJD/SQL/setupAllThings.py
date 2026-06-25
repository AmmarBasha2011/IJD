import os
import json
from ..functions.createFolder import createFolder
from ..functions.writeJsonContent import writeJsonContent
from ..functions.getJsonContent import getJsonContent

def setupAllThings():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    createFolder(json_dir)
    # Check if tables.json already exists and is valid
    try:
        content = getJsonContent("tables")
        if "tables" not in content:
            writeJsonContent({"tables": {}}, "tables")
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        # If not, create it with empty tables dict
        writeJsonContent({"tables": {}}, "tables")
