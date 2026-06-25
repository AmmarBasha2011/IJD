import gzip
import json
import os
from base64 import b64encode, b64decode


def compress_data(data):
    """Compress JSON data using gzip!"""
    json_str = json.dumps(data)
    compressed = gzip.compress(json_str.encode("utf-8"))
    return b64encode(compressed).decode("utf-8")


def decompress_data(compressed_str):
    """Decompress data compressed with compress_data!"""
    compressed = b64decode(compressed_str.encode("utf-8"))
    json_str = gzip.decompress(compressed).decode("utf-8")
    return json.loads(json_str)


class SimpleAES:
    """Simple encryption wrapper using cryptography (Fernet)!"""
    
    @staticmethod
    def generate_key():
        try:
            from cryptography.fernet import Fernet
        except ImportError:
            raise ImportError("cryptography is required for encryption!")
        return Fernet.generate_key().decode("utf-8")
    
    @staticmethod
    def encrypt_data(data, key):
        try:
            from cryptography.fernet import Fernet
        except ImportError:
            raise ImportError("cryptography is required for encryption!")
        
        fernet = Fernet(key.encode("utf-8"))
        json_str = json.dumps(data)
        encrypted = fernet.encrypt(json_str.encode("utf-8"))
        return b64encode(encrypted).decode("utf-8")
    
    @staticmethod
    def decrypt_data(encrypted_str, key):
        try:
            from cryptography.fernet import Fernet
        except ImportError:
            raise ImportError("cryptography is required for encryption!")
        
        encrypted = b64decode(encrypted_str.encode("utf-8"))
        fernet = Fernet(key.encode("utf-8"))
        json_str = fernet.decrypt(encrypted).decode("utf-8")
        return json.loads(json_str)


def save_compressed_table(table_name, data):
    from .writeJsonContent import writeJsonContent
    compressed = compress_data(data)
    writeJsonContent({"__compressed__": True, "data": compressed}, table_name)


def load_compressed_table(table_name):
    from .getJsonContent import getJsonContent
    data = getJsonContent(table_name)
    if data.get("__compressed__"):
        return decompress_data(data["data"])
    return data


def save_encrypted_table(table_name, data, key):
    from .writeJsonContent import writeJsonContent
    encrypted = SimpleAES.encrypt_data(data, key)
    writeJsonContent({"__encrypted__": True, "data": encrypted}, table_name)


def load_encrypted_table(table_name, key):
    from .getJsonContent import getJsonContent
    data = getJsonContent(table_name)
    if data.get("__encrypted__"):
        return SimpleAES.decrypt_data(data["data"], key)
    return data
