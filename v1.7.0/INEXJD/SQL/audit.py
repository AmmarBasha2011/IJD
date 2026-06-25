import os
import json
import datetime
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def _get_audit_log_dir():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    audit_dir = os.path.join(base_dir, "audit_logs")
    os.makedirs(audit_dir, exist_ok=True)
    return audit_dir


def _get_audit_log_file(table_name):
    audit_dir = _get_audit_log_dir()
    return os.path.join(audit_dir, f"{table_name}_audit.json")


def _get_audit_log(table_name):
    log_file = _get_audit_log_file(table_name)
    if not os.path.exists(log_file):
        return []
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def _save_audit_log(table_name, logs):
    log_file = _get_audit_log_file(table_name)
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, default=str)


def log_action(table_name, action, details=None):
    """
    Log an action performed on a table!
    """
    logs = _get_audit_log(table_name)
    log_entry = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "action": action,
        "details": details or {},
    }
    logs.append(log_entry)
    _save_audit_log(table_name, logs)
    return True


def get_audit_log(table_name, limit=None, offset=0):
    """
    Get audit log entries, optionally paginated!
    """
    logs = _get_audit_log(table_name)
    if not limit:
        return logs[offset:]
    return logs[offset:offset+limit]


def clear_audit_log(table_name):
    """
    Clear audit log for a table!
    """
    _save_audit_log(table_name, [])
    return True
