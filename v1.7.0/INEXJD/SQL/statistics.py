from ..functions.getJsonContent import getJsonContent
from ..SQL.getTables import getTables
from ..functions.logger import get_logger
import os


def get_table_statistics(table_name):
    """
    Get detailed statistics for a single table!
    """
    data = getJsonContent(table_name)
    stats = {
        "table_name": table_name,
        "record_count": len(data),
        "fields": [],
        "field_stats": {},
        "size_bytes": 0
    }

    if not data:
        return stats

    # Get all fields
    fields = list(data[0].keys())
    stats["fields"] = fields

    # Calculate field stats
    for field in fields:
        values = [record.get(field) for record in data if record.get(field) is not None]
        field_stat = {
            "non_null_count": len(values),
            "null_count": len(data) - len(values)
        }
        
        # Try numeric stats if applicable
        numeric_vals = [v for v in values if isinstance(v, (int, float))]
        if numeric_vals:
            field_stat["type"] = "numeric"
            field_stat["min"] = min(numeric_vals)
            field_stat["max"] = max(numeric_vals)
            field_stat["avg"] = sum(numeric_vals) / len(numeric_vals)
            field_stat["sum"] = sum(numeric_vals)
        else:
            field_stat["type"] = "other"
        
        # Unique count
        unique_vals = set()
        for v in values:
            unique_vals.add(str(v) if isinstance(v, (list, dict)) else v)
        field_stat["unique_count"] = len(unique_vals)
        
        stats["field_stats"][field] = field_stat

    # Estimate size
    import json
    stats["size_bytes"] = len(json.dumps(data))
    return stats


def get_database_statistics():
    """
    Get overall database statistics!
    """
    tables = getTables().get("tables", {})
    db_stats = {
        "table_count": len(tables),
        "total_records": 0,
        "total_size_bytes": 0,
        "tables": {}
    }

    for table in tables:
        table_stat = get_table_statistics(table)
        db_stats["total_records"] += table_stat["record_count"]
        db_stats["total_size_bytes"] += table_stat["size_bytes"]
        db_stats["tables"][table] = table_stat

    return db_stats


def get_usage_report():
    """
    Generate a human-readable usage report!
    """
    db_stats = get_database_statistics()
    report_lines = []
    report_lines.append("INEXJD Database Usage Report")
    report_lines.append("=" * 40)
    report_lines.append(f"Tables: {db_stats['table_count']}")
    report_lines.append(f"Total records: {db_stats['total_records']}")
    report_lines.append(f"Total size: {db_stats['total_size_bytes'] / 1024:.2f} KB")
    report_lines.append("")
    for table_name, table_stat in db_stats["tables"].items():
        report_lines.append(f"📊 {table_name}:")
        report_lines.append(f"   Records: {table_stat['record_count']}")
        report_lines.append(f"   Size: {table_stat['size_bytes'] / 1024:.2f} KB")
        report_lines.append(f"   Fields: {', '.join(table_stat['fields'])}")
        report_lines.append("")
    return "\n".join(report_lines)
