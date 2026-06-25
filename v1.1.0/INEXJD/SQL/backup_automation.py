import os
import time
import threading
import json
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


_auto_backup_enabled = False
_auto_backup_thread = None
_auto_backup_interval = 3600  # Default 1 hour
_auto_backup_dir = None


def _get_auto_backup_dir():
    global _auto_backup_dir
    if _auto_backup_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _auto_backup_dir = os.path.join(base_dir, "Json", "backups")
    os.makedirs(_auto_backup_dir, exist_ok=True)
    return _auto_backup_dir


def _auto_backup_job():
    while _auto_backup_enabled:
        try:
            backup_all_tables()
        except Exception as e:
            print(f"Auto-backup failed: {e}")
        time.sleep(_auto_backup_interval)


def enable_auto_backup(interval=3600, backup_dir=None):
    global _auto_backup_enabled, _auto_backup_interval, _auto_backup_dir, _auto_backup_thread
    if backup_dir is not None:
        _auto_backup_dir = backup_dir
    _auto_backup_interval = interval
    _auto_backup_enabled = True
    if _auto_backup_thread is None or not _auto_backup_thread.is_alive():
        _auto_backup_thread = threading.Thread(target=_auto_backup_job, daemon=True)
        _auto_backup_thread.start()


def disable_auto_backup():
    global _auto_backup_enabled
    _auto_backup_enabled = False


def backup_all_tables():
    backup_dir = _get_auto_backup_dir()
    timestamp = int(time.time())
    
    tables_data = getJsonContent("tables")
    for table_name in tables_data.get("tables", {}):
        try:
            data = getJsonContent(table_name)
            backup_path = os.path.join(backup_dir, f"{table_name}_{timestamp}.json")
            with open(backup_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Failed to backup {table_name}: {e}")
    # Backup tables.json too
    tables_backup_path = os.path.join(backup_dir, f"tables_{timestamp}.json")
    with open(tables_backup_path, 'w') as f:
        json.dump(tables_data, f, indent=4)


def list_backups(table_name=None):
    backup_dir = _get_auto_backup_dir()
    backups = []
    for f in os.listdir(backup_dir):
        if table_name and not f.startswith(f"{table_name}_"):
            continue
        try:
            ts = int(f.split('_')[-1].split('.')[0])
            backups.append((ts, os.path.join(backup_dir, f)))
        except:
            pass
    backups.sort(reverse=True, key=lambda x: x[0])
    return backups


def restore_from_latest_backup(table_name):
    backups = list_backups(table_name)
    if not backups:
        return "No backups found"
    latest_backup = backups[0][1]
    with open(latest_backup, 'r') as f:
        data = json.load(f)
    writeJsonContent(data, table_name)
    return "Restored from latest backup"
