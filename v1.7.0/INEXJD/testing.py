import tempfile
import shutil
import os
from .SQL.deleteAllTables import deleteAllTables
from .SQL.createTable import createTable
from .functions.getJsonContent import getJsonContent


class INEXJDTestContext:
    """
    Context manager for safe testing with temporary directories!
    """
    def __init__(self):
        self.temp_dir = None
        self.original_json_dir = None

    def __enter__(self):
        # Create temp dir
        self.temp_dir = tempfile.mkdtemp(prefix="inexjd_test_")
        
        # Save original getJsonContent dir logic if needed,
        # For simplicity let's create a test tables.json in temp dir
        # and use it as test base
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup
        if self.temp_dir and os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


# Pytest fixtures
def pytest_fixture_inexjd_empty():
    """
    Pytest fixture that provides a clean, empty INEXJD environment!
    """
    import pytest
    @pytest.fixture
    def clean_inexjd():
        # Reset everything
        deleteAllTables()
        yield
        deleteAllTables()
    return clean_inexjd


def setup_test_tables():
    """
    Helper function to set up common test tables!
    """
    deleteAllTables()
    
    # Create test users
    createTable("test_users", ["id", "name", "email", "age", "active"])
    
    # Create test orders
    createTable("test_orders", ["id", "user_id", "product", "amount"])
    
    return True


def sample_test_data():
    """
    Returns sample test data for quick tests!
    """
    users = [
        {"id": 1, "name": "Alice", "email": "alice@test.com", "age": 30, "active": True},
        {"id": 2, "name": "Bob", "email": "bob@test.com", "age": 25, "active": True},
        {"id": 3, "name": "Charlie", "email": "charlie@test.com", "age": 35, "active": False}
    ]
    
    orders = [
        {"id": 1, "user_id": 1, "product": "Laptop", "amount": 999.99},
        {"id": 2, "user_id": 1, "product": "Mouse", "amount": 25.50},
        {"id": 3, "user_id": 2, "product": "Phone", "amount": 699.00}
    ]
    return {"users": users, "orders": orders}
