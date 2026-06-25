import json
import os
import time
import fcntl
import msvcrt


def getJsonContent(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_dir = os.path.join(base_dir, "Json")
    file_path = os.path.join(json_dir, f"{file_name}.json")
    lock_path = f"{file_path}.lock"
    
    max_retries = 10
    retry_delay = 0.1
    
    for attempt in range(max_retries):
        try:
            lock_file = open(lock_path, 'w')
            if os.name == 'nt':
                msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                fcntl.flock(lock_file, fcntl.LOCK_SH | fcntl.LOCK_NB)
            
            try:
                with open(file_path, 'r') as file:
                    file_content = file.read()
                
                json_data = json.loads(file_content)
                if not isinstance(json_data, (dict, list)):
                    raise ValueError("Content is not JSON data")
                
                return json_data
            finally:
                if os.name == 'nt':
                    msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    fcntl.flock(lock_file, fcntl.LOCK_UN)
                lock_file.close()
                if os.path.exists(lock_path):
                    try:
                        os.remove(lock_path)
                    except:
                        pass
        except (IOError, BlockingIOError):
            time.sleep(retry_delay)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_name}.json not found in Json directory")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {str(e)}")
        except Exception as e:
            print(f"Error reading JSON file: {str(e)}")
            if 'lock_file' in locals():
                lock_file.close()
                if os.path.exists(lock_path):
                    try:
                        os.remove(lock_path)
                    except:
                        pass
            raise
    
    raise RuntimeError(f"Failed to acquire lock for {file_path} after {max_retries} attempts")