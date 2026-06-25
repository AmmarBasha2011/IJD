import os
import json
from .SQL.getTables import getTables
from .functions.getJsonContent import getJsonContent
from .functions.logger import get_logger


def check_file_integrity(table_name):
    try:
        getJsonContent(table_name)
        return True, None
    except Exception as e:
        return False, str(e)


def run_diagnostics():
    logger = get_logger()
    report = {
        "status": "healthy",
        "checks": {},
        "warnings": []
    }

    # 1. Check if tables.json exists
    logger.info("Checking tables.json...")
    try:
        tables_data = getTables()
        report["checks"]["tables_json"] = "ok"
    except Exception as e:
        report["status"] = "unhealthy"
        report["checks"]["tables_json"] = f"failed: {str(e)}"
        return report

    tables = tables_data.get("tables", {})
    report["checks"]["table_count"] = len(tables)

    # 2. Check all individual table files
    for table_name in tables:
        ok, err = check_file_integrity(table_name)
        if ok:
            report["checks"][f"table_{table_name}"] = "ok"
        else:
            report["status"] = "unhealthy"
            report["checks"][f"table_{table_name}"] = f"failed: {err}"

    # 3. Check disk space (simple)
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if os.name == "nt":
            import ctypes
            free_bytes = ctypes.c_ulonglong(0)
            total_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                ctypes.c_wchar_p(base_dir), None,
                ctypes.pointer(total_bytes), ctypes.pointer(free_bytes)
            )
            free_mb = free_bytes.value / (1024 * 1024)
            if free_mb < 100:
                report["warnings"].append(f"Low disk space: {free_mb:.1f} MB left")
        else:
            statvfs = os.statvfs(base_dir)
            free_mb = (statvfs.f_frsize * statvfs.f_bavail) / (1024 * 1024)
            if free_mb < 100:
                report["warnings"].append(f"Low disk space: {free_mb:.1f} MB left")
        report["checks"]["disk_space"] = "ok"
    except Exception as e:
        report["checks"]["disk_space"] = f"unable to check: {str(e)}"

    return report


def is_database_healthy():
    diag = run_diagnostics()
    return diag["status"] == "healthy"
