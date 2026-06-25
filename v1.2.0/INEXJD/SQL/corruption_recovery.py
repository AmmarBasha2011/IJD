import os
import json
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def check_corruption(file_name):
    """
    Check if a file is corrupted.
    
    Args:
        file_name (str): Name of the file without .json
    
    Returns:
        bool: True if corrupted, False otherwise
    """
    try:
        getJsonContent(file_name)
        return False
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return True


def create_backup(file_name, backup_path=None):
    """
    Create a backup of a file.
    
    Args:
        file_name (str): Name of the file without .json
        backup_path (str, optional): Path to save backup
    
    Returns:
        str: Path to backup file
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    file_path = os.path.join(json_dir, f"{file_name}.json")
    
    if backup_path is None:
        timestamp = int(time.time())
        backup_path = os.path.join(json_dir, f"{file_name}_backup_{timestamp}.json")
    
    with open(file_path, 'r') as f_in, open(backup_path, 'w') as f_out:
        f_out.write(f_in.read())
    
    return backup_path


def recover_from_backup(file_name, backup_path):
    """
    Recover a file from backup.
    
    Args:
        file_name (str): Name of the file without .json
        backup_path (str): Path to backup file
    
    Returns:
        str: Result message
    """
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        
        writeJsonContent(data, file_name)
        return "File recovered successfully from backup"
    except Exception as e:
        return f"Recovery failed: {str(e)}"


def auto_recover(file_name):
    """
    Automatically try to recover a corrupted file by finding the latest backup.
    
    Args:
        file_name (str): Name of the file without .json
    
    Returns:
        str: Result message
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    
    backups = []
    for f in os.listdir(json_dir):
        if f.startswith(f"{file_name}_backup_") and f.endswith(".json"):
            try:
                ts = int(f.split('_')[-1].split('.')[0])
                backups.append((ts, os.path.join(json_dir, f)))
            except:
                pass
    
    if not backups:
        return "No backups found for recovery"
    
    backups.sort(reverse=True)
    latest_backup = backups[0][1]
    
    return recover_from_backup(file_name, latest_backup)


import time
