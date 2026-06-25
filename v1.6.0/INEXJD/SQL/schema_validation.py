import os
import json
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def _get_auto_increment_file(table_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    counter_dir = os.path.join(base_dir, "counters")
    os.makedirs(counter_dir, exist_ok=True)
    return os.path.join(counter_dir, f"{table_name}_auto.json")


def _get_next_auto_id(table_name, field_name):
    """Get next auto-increment ID for a field."""
    counter_file = _get_auto_increment_file(table_name)
    counters = {}
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            counters = json.load(f)
    next_id = counters.get(field_name, 1)
    counters[field_name] = next_id + 1
    with open(counter_file, "w") as f:
        json.dump(counters, f)
    return next_id


def _reset_auto_id(table_name, field_name, start=1):
    """Reset auto-increment counter for a field."""
    counter_file = _get_auto_increment_file(table_name)
    counters = {}
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            counters = json.load(f)
    counters[field_name] = start
    with open(counter_file, "w") as f:
        json.dump(counters, f)


def define_table_schema(table_name, schema):
    """
    Define a schema for a table and save it.
    
    Args:
        table_name (str): Target table
        schema (dict): Schema definition like {
            "id": {"type": "int", "auto_increment": True, "primary_key": True},
            "name": {"type": "str", "required": True, "unique": True},
            "status": {"type": "str", "default": "active"}
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


def validate_record(record, schema, table_name=None):
    """
    Validate a single record against a schema, apply defaults and auto-increment.
    
    Returns:
        tuple: (is_valid, errors, processed_record)
    """
    errors = []
    processed_record = record.copy()
    
    for field, field_schema in schema.items():
        value = processed_record.get(field)
        
        # Auto-increment
        if field_schema.get("auto_increment") and value is None:
            if not table_name:
                errors.append("Auto-increment requires table_name parameter")
                continue
            processed_record[field] = _get_next_auto_id(table_name, field)
            value = processed_record[field]
        
        # Default value
        if value is None and "default" in field_schema:
            processed_record[field] = field_schema["default"]
            value = processed_record[field]
        
        # Required field check
        if field_schema.get("required", False) and value is None:
            errors.append(f"Field '{field}' is required")
            continue
        
        # Type check (Typed Columns)
        if value is not None:
            expected_type = field_schema.get("type")
            type_mapping = {
                "int": int,
                "float": float,
                "str": str,
                "bool": bool,
                "list": list,
                "dict": dict,
                "datetime": str
            }
            if expected_type and not isinstance(value, type_mapping.get(expected_type)):
                errors.append(f"Field '{field}' should be {expected_type}, got {type(value).__name__}")
    
    # Unique constraint check
    if table_name:
        for field, field_schema in schema.items():
            if field_schema.get("unique") and processed_record.get(field) is not None:
                table_data = getJsonContent(table_name)
                for r in table_data:
                    if r.get(field) == processed_record[field]:
                        errors.append(f"Field '{field}' must be unique, value '{processed_record[field]}' already exists")
                        break
    
    return len(errors) == 0, errors, processed_record


def validate_and_insert(table_name, record):
    """Validate, apply defaults/auto-increment, then insert a single record if valid."""
    schema = get_table_schema(table_name)
    if not schema:
        raise ValueError(f"No schema defined for {table_name}")
    
    valid, errors, processed_record = validate_record(record, schema, table_name)
    if not valid:
        return f"Validation failed: {', '.join(errors)}"
    
    from .insertTableData import insertTableData
    return insertTableData(table_name, processed_record)


def validate_table(table_name):
    """Validate all existing records in a table against defined schema."""
    schema = get_table_schema(table_name)
    if not schema:
        return f"No schema defined for {table_name}"
    
    table_data = getJsonContent(table_name)
    all_valid = True
    for i, record in enumerate(table_data):
        valid, errors, _ = validate_record(record, schema)
        if not valid:
            print(f"Record {i} invalid: {errors}")
            all_valid = False
    return "All records valid" if all_valid else "Some records invalid"
