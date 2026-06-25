import os
import json
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def _get_relationships_file():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "relationships.json")


def define_relationship(from_table, from_field, to_table, to_field, rel_type="one_to_many"):
    """
    Define a relationship between tables!
    """
    rel_file = _get_relationships_file()
    relationships = {}
    if os.path.exists(rel_file):
        with open(rel_file, "r") as f:
            relationships = json.load(f)
    rel_key = f"{from_table}.{from_field}->{to_table}.{to_field}"
    relationships[rel_key] = {
        "from_table": from_table,
        "from_field": from_field,
        "to_table": to_table,
        "to_field": to_field,
        "type": rel_type
    }
    with open(rel_file, "w") as f:
        json.dump(relationships, f, indent=2)
    return True


def get_related_records(from_table, from_record, to_table):
    """
    Get related records from another table!
    """
    rel_file = _get_relationships_file()
    relationships = {}
    if os.path.exists(rel_file):
        with open(rel_file, "r") as f:
            relationships = json.load(f)
    # Find matching relationship
    for rel in relationships.values():
        if rel["from_table"] == from_table and rel["to_table"] == to_table:
            from_val = from_record.get(rel["from_field"])
            to_data = getJsonContent(to_table)
            return [r for r in to_data if r.get(rel["to_field"]) == from_val]
    return []
