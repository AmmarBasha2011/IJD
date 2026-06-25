import os
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent

_active_transaction = None
_transaction_log = []


def begin_transaction():
    """
    Begin a new transaction. Saves current state of all tables for rollback.
    """
    global _active_transaction, _transaction_log
    
    if _active_transaction is not None:
        raise RuntimeError("A transaction is already active")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    
    _active_transaction = True
    _transaction_log = []
    
    # Save current state of all tables
    tables_data = getJsonContent("tables")
    for table_name in tables_data.get("tables", {}):
        try:
            data = getJsonContent(table_name)
            _transaction_log.append((table_name, data.copy() if isinstance(data, list) else data))
        except FileNotFoundError:
            pass
    
    # Save tables.json state too
    _transaction_log.append(("tables", tables_data.copy()))
    
    return True


def commit():
    """
    Commit the active transaction. All changes become permanent.
    """
    global _active_transaction, _transaction_log
    
    if _active_transaction is None:
        raise RuntimeError("No active transaction to commit")
    
    _active_transaction = None
    _transaction_log = []
    
    return True


def rollback():
    """
    Rollback the active transaction. Reverts all changes since begin_transaction().
    """
    global _active_transaction, _transaction_log
    
    if _active_transaction is None:
        raise RuntimeError("No active transaction to rollback")
    
    # Restore all saved states
    for table_name, saved_data in _transaction_log:
        writeJsonContent(saved_data, table_name)
    
    _active_transaction = None
    _transaction_log = []
    
    return True


def is_transaction_active():
    """
    Check if a transaction is currently active.
    """
    return _active_transaction is not None
