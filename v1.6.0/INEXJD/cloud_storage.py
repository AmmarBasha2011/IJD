"""
Cloud Storage Backends for INEXJD!
Supports S3, Dropbox (simple implementations)!
"""
import json
import os


class CloudStorageBackend:
    """Base class for all cloud storage backends!"""
    def upload_file(self, local_path, remote_path):
        raise NotImplementedError
    def download_file(self, remote_path, local_path):
        raise NotImplementedError
    def list_files(self, prefix=""):
        raise NotImplementedError


class S3Backend(CloudStorageBackend):
    """
    Backend for Amazon S3 (or S3-compatible storage)!
    Requires boto3!
    """
    def __init__(self, bucket, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
        self.bucket = bucket
        try:
            import boto3
        except ImportError:
            raise ImportError("boto3 is required for S3 backend")
        
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
    
    def upload_file(self, local_path, remote_path):
        self.s3.upload_file(local_path, self.bucket, remote_path)
        return True
    
    def download_file(self, remote_path, local_path):
        self.s3.download_file(self.bucket, remote_path, local_path)
        return True
    
    def list_files(self, prefix=""):
        response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix=prefix)
        if 'Contents' in response:
            return [obj['Key'] for obj in response['Contents']]
        return []


class DropboxBackend(CloudStorageBackend):
    """
    Dropbox backend! Requires dropbox!
    """
    def __init__(self, access_token):
        try:
            import dropbox
        except ImportError:
            raise ImportError("dropbox is required for Dropbox backend")
        
        self.dbx = dropbox.Dropbox(access_token)
    
    def upload_file(self, local_path, remote_path):
        with open(local_path, "rb") as f:
            self.dbx.files_upload(f.read(), remote_path, mode=dropbox.files.WriteMode.overwrite)
        return True
    
    def download_file(self, remote_path, local_path):
        _, res = self.dbx.files_download(remote_path)
        with open(local_path, "wb") as f:
            f.write(res.content)
        return True


class GoogleDriveBackend(CloudStorageBackend):
    """
    Placeholder for Google Drive backend!
    Requires google-api-python-client and oauth2client!
    """
    def __init__(self, credentials_path=None):
        pass


def backup_to_cloud(backend: CloudStorageBackend, tables, backup_name=None):
    """Helper function for backing up all tables to a cloud backend!"""
    import time
    from .functions.getJsonContent import getJsonContent
    from .SQL.getTables import getTables
    
    ts = backup_name or f"inexjd_backup_{int(time.time())}"
    tables_data = getTables()
    for table in tables_data.get("tables", {}):
        data = getJsonContent(table)
        local_path = f"/tmp/inexjd_{table}.json"
        with open(local_path, "w") as f:
            json.dump(data, f)
        backend.upload_file(local_path, f"{ts}/{table}.json")
    return ts
