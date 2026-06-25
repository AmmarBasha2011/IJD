import os
import json
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def define_table_schema(table_name, schema):
    """
    Define a schema for a table and save it.
    
    Args:
        table_name (str): Target table
        schema (dict): Schema definition like {
            "field1": {"type": "int", "required": True},
            "field2": {"type": "str", "default": "N/A"}
        }
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_dir = os.path.join(base_dir, "schemas")
    os.makedirs(schema_dir, exist_ok=True)
    schema_file = os.path.join(schema_dir, f"{table_name}.json")
    
    with open(schema_file, "w", encoding="utf-8") as f:
        json.dump(schema, f, ensure_ascii=False, indent=4)
    return f"Schema defined for {table_name}"


def get_table_schema(table_name):
    """Get defined schema for a table."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_file = os.path.join(base_dir, "schemas", f"{table_name}.json")
    if not os.path.exists(schema_file):
        return None
    with open(schema_file, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_record(record, schema):
    """
    Validate a single record against a schema.
    
    Returns:
        tuple: (is_valid, errors)
    """
    errors = []
    for field, field_schema in schema.items():
        value = record.get(field)
        
        if field_schema.get("required", False) and value is None:
            errors.append(f"Field '{field}' is required")
            continue
        
        if value is not None:
            expected_type = field_schema.get("type")
            type_mapping = {
                "int": int,
                "float": float,
                "str": str,
                "bool": bool,
                "list": list,
                "dict": dict
            }
            if expected_type and not isinstance(value, type_mapping.get(expected_type)):
                errors.append(f"Field '{field}' should be {expected_type}, got {type(value).__name__}")
    return len(errors) == 0, errors


def validate_and_insert(table_name, record):
    """Validate then insert a single record if valid."""
    schema = get_table_schema(table_name)
    if not schema:
        raise ValueError(f"No schema defined for {table_name}")
    
    valid, errors = validate_record(record, schema)
    if not valid:
        return f"Validation failed: {', '.join(errors)}"
    
    from .insertTableData import insertTableData
    return insertTableData(table_name, record)


def validate_table(table_name):
    """Validate all existing records in a table against defined schema."""
    schema = get_table_schema(table_name)
    if not schema:
        return f"No schema defined for {table_name}"
    
    table_data = getJsonContent(table_name)
    all_valid = True
    for i, record in enumerate(table_data):
        valid, errors = validate_record(record, schema)
        if not valid:
            print(f"Record {i} invalid: {errors}")
            all_valid = False
    return "All records valid" if all_valid else "Some records invalid"
