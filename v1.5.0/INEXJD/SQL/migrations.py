import os
import json
import datetime
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def _get_migrations_dir():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    migrations_dir = os.path.join(base_dir, "migrations")
    os.makedirs(migrations_dir, exist_ok=True)
    return migrations_dir


def _get_version_file(table_name):
    migrations_dir = _get_migrations_dir()
    return os.path.join(migrations_dir, f"{table_name}_versions.json")


def get_current_version(table_name):
    """Get current schema version for a table."""
    version_file = _get_version_file(table_name)
    if not os.path.exists(version_file):
        return 0
    with open(version_file, "r") as f:
        data = json.load(f)
        return data.get("current_version", 0)


def set_current_version(table_name, version):
    """Set current schema version for a table."""
    version_file = _get_version_file(table_name)
    data = {"current_version": version, "last_updated": datetime.datetime.now().isoformat()}
    with open(version_file, "w") as f:
        json.dump(data, f, indent=4)


def create_migration(table_name, version, up_function, down_function=None, description=""):
    """
    Create a new migration for a table.
    
    Args:
        table_name (str): Target table
        version (int): Migration version number
        up_function (callable): Function to apply migration
        down_function (callable, optional): Function to roll back migration
        description (str, optional): Migration description
    """
    migrations_dir = _get_migrations_dir()
    migration_file = os.path.join(migrations_dir, f"{table_name}_v{version}.json")
    
    migration_data = {
        "version": version,
        "description": description,
        "created_at": datetime.datetime.now().isoformat(),
    }
    
    with open(migration_file, "w") as f:
        json.dump(migration_data, f, indent=4)
    
    # Save the functions as separate Python files (simple implementation)
    up_file = os.path.join(migrations_dir, f"{table_name}_v{version}_up.py")
    down_file = os.path.join(migrations_dir, f"{table_name}_v{version}_down.py")
    
    import inspect
    with open(up_file, "w") as f:
        f.write("# Up migration function\n")
        f.write(inspect.getsource(up_function))
    
    if down_function:
        with open(down_file, "w") as f:
            f.write("# Down migration function\n")
            f.write(inspect.getsource(down_function))
    
    return f"Migration {version} created for {table_name}"


def apply_migration(table_name, version, up=True):
    """
    Apply or roll back a migration.
    
    Args:
        table_name (str): Target table
        version (int): Migration version
        up (bool): True to apply, False to roll back
    """
    migrations_dir = _get_migrations_dir()
    file_suffix = "up" if up else "down"
    migration_file = os.path.join(migrations_dir, f"{table_name}_v{version}_{file_suffix}.py")
    
    if not os.path.exists(migration_file):
        return f"Migration {version} {file_suffix} not found"
    
    # Simple way to execute migration: import and run
    import sys
    sys.path.insert(0, migrations_dir)
    module_name = f"{table_name}_v{version}_{file_suffix}"
    try:
        # Read the file content and execute it
        with open(migration_file, "r") as f:
            exec(f.read(), globals())
        # Get the function (should be named 'migrate' or similar)
        func_name = "migrate"
        if func_name in globals():
            globals()[func_name](table_name)
            set_current_version(table_name, version if up else version - 1)
            return f"Migration {version} {'applied' if up else 'rolled back'} successfully"
        else:
            return f"No 'migrate' function found in migration file"
    except Exception as e:
        return f"Migration failed: {str(e)}"


# Helper migration functions
def add_column(table_name, column_name, default_value=None):
    """Add a new column to a table."""
    table_data = getJsonContent(table_name)
    for record in table_data:
        if column_name not in record:
            record[column_name] = default_value
    writeJsonContent(table_data, table_name)
    return f"Column {column_name} added"


def drop_column(table_name, column_name):
    """Drop a column from a table."""
    table_data = getJsonContent(table_name)
    for record in table_data:
        if column_name in record:
            del record[column_name]
    writeJsonContent(table_data, table_name)
    return f"Column {column_name} dropped"


def rename_column(table_name, old_name, new_name):
    """Rename a column in a table."""
    table_data = getJsonContent(table_name)
    for record in table_data:
        if old_name in record:
            record[new_name] = record[old_name]
            del record[old_name]
    writeJsonContent(table_data, table_name)
    return f"Column {old_name} renamed to {new_name}"


def apply_pending_migrations(table_name, target_version=None):
    """
    Auto-apply all pending migrations up to target_version!
    """
    current = get_current_version(table_name)
    migrations_dir = _get_migrations_dir()
    
    # Find all up migrations for this table
    import glob
    pattern = os.path.join(migrations_dir, f"{table_name}_v*_up.py")
    migration_files = sorted(glob.glob(pattern))
    
    applied = []
    for mf in migration_files:
        # Extract version number from filename
        base = os.path.basename(mf)
        parts = base.split("_v")
        if len(parts) <2:
            continue
        ver_str = parts[1].split("_")[0]
        try:
            ver = int(ver_str)
        except ValueError:
            continue
        
        if ver > current:
            if target_version is None or ver <= target_version:
                res = apply_migration(table_name, ver, up=True)
                applied.append(ver)
                print(f"Applied migration v{ver}")
    
    return applied


def get_migration_history(table_name):
    """
    Get history of applied migrations!
    """
    from .getTables import getTables
    return {"current_version": get_current_version(table_name)}

