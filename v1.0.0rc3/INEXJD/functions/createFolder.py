import os
import logging

def createFolder(folder_path):
    """
    Create a folder at the specified path if it doesn't exist.
    
    Args:
        folder_path (str): The path where the folder should be created
        
    Returns:
        bool: True if folder was created or already exists, False if creation failed
    """
    try:
        # Check if folder doesn't exist
        if not os.path.exists(folder_path):
            # Create folder
            os.makedirs(folder_path)
            logging.info(f"Created folder: {folder_path}")
            return True
        else:
            logging.info(f"Folder already exists: {folder_path}")
            return True
            
    except Exception as e:
        logging.error(f"Error creating folder {folder_path}: {str(e)}")
        return False