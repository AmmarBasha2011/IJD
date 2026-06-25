import json
import os
import time
import fcntl  # For Unix-based systems
import msvcrt  # For Windows


def writeJsonContent(data, file_name):
    """
    Write JSON content to a file with file locking for concurrency safety.
    
    Args:
        data: The data to be written as JSON
        file_name (str): The name of the file (without .json extension) where JSON will be written
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    os.makedirs(json_dir, exist_ok=True)
    file_path = os.path.join(json_dir, f"{file_name}.json")
    lock_path = f"{file_path}.lock"
    
    max_retries = 10
    retry_delay = 0.1  # Seconds
    
    for attempt in range(max_retries):
        try:
            lock_file = open(lock_path, 'wb')
            if os.name == 'nt':  # Windows
                msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
            else:  # Unix-based
                fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            
            if os.name == 'nt':
                msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(lock_file, fcntl.LOCK_UN)
            lock_file.close()
            
            if os.path.exists(lock_path):
                os.remove(lock_path)
            
            return True
        except (IOError, BlockingIOError):
            time.sleep(retry_delay)
        except Exception as e:
            print(f"Error writing JSON file: {str(e)}")
            if 'lock_file' in locals():
                lock_file.close()
            if os.path.exists(lock_path):
                try:
                    os.remove(lock_path)
                except:
                    pass
            return False
    
    print(f"Failed to acquire lock for {file_path} after {max_retries} attempts")
    return False