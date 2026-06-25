# INEXJD - JSON SQL-like Database Library

A lightweight, file-based JSON database library with SQL-like operations and advanced features!


## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Features](#features)
    - [v1.0.0 - Core Features](#v100---core-features)
    - [v1.1.0 - Reliability & Performance](#v110---reliability--performance)
    - [v1.2.0 - Querying & Schema](#v120---querying--schema)
    - [v1.3.0 - Schema Management](#v130---schema-management)
    - [v1.4.0 - ORM, Web & Tools](#v140---orm-web--tools)
    - [v1.5.0 - Import/Export & Integrations](#v150---importexport--integrations)
    - [v1.6.0 - Security & Monitoring](#v160---security--monitoring)
    - [v1.7.0 - Advanced Querying](#v170---advanced-querying)


## Installation
```bash
# Basic installation
pip install INEXJD

# Optional extras
pip install INEXJD[gui,excel,encryption]
```


## Quick Start
```python
import INEXJD

# Create a table
INEXJD.createTable("users", ["id", "name", "email"])

# Insert a record
INEXJD.insertTableData("users", {"id": 1, "name": "Alice", "email": "alice@example.com"})

# Get data
print(INEXJD.getTableData("users"))
```


## Features


### v1.0.0 - Core Features
- **Create/Delete Tables**: `createTable`, `deleteTable`
- **CRUD Operations**: `insertTableData`, `updateTableData`, `deleteTableData`, `getTableData`
- **Querying**: `filterRecords`, `searchTableData`, `getRecordById`
- **Aggregation**: `countTableData`, `countRecordsByCondition`, `aggregateTableData`


### v1.1.0 - Reliability & Performance
- **Transactions**: `begin_transaction()`, `commit()`, `rollback()`
- **Concurrency Safety**: File locking for multi-process access
- **Indexing**: `create_index()`, `drop_index()`, `search_with_index()`
- **Caching**: `cache_get()`, `cache_put()`, `cache_config()`
- **Backup Automation**: `enable_auto_backup()`, `backup_all_tables()`
- **Corruption Recovery**: `check_corruption()`, `auto_recover()`


### v1.2.0 - Querying & Schema
- **SQL-like Queries**: `execute_query()`
- **Bulk Operations**: `bulk_insert()`, `bulk_update()`, `bulk_delete()`
- **Pagination**: `paginate()`, `get_page_count()`
- **Sorting**: `sort_by_multiple()`
- **Distinct Values**: `get_distinct()`
- **Joins**: `join()`
- **Subqueries**: `subquery_in()`, `exists_subquery()`
- **Schema Validation**: `define_table_schema()`, `validate_and_insert()`


### v1.3.0 - Schema Management
- **Typed Columns**: Enforce `int`, `float`, `str`, `bool`, etc.
- **Auto-increment IDs**: Automatic unique ID generation
- **Unique Constraints**: Ensure no duplicate values
- **Default Values**: Set defaults for missing fields
- **Schema Migrations**: `create_migration()`, `apply_pending_migrations()`


### v1.4.0 - ORM, Web & Tools
- **ORM**:
  ```python
  from INEXJD import Model
  class User(Model):
      _table_name = "users"

  user = User.create(name="Bob", email="bob@example.com")
  user.save()
  ```
- **CLI Tool**:
  ```bash
  # List tables
  inexjd list
  # Query tables
  inexjd query "SELECT * FROM users"
  ```
- **Web GUI Admin**: `INEXJD.run_gui()` (starts a Flask-based admin interface at `http://localhost:5000`)


### v1.5.0 - Import/Export & Integrations
- **Import/Export Formats**:
  ```python
  # CSV
  INEXJD.export_csv(data, "data.csv")
  imported = INEXJD.import_csv("data.csv")

  # XML
  INEXJD.export_xml(data, "data.xml")
  imported = INEXJD.import_xml("data.xml")

  # Excel (requires `openpyxl`)
  INEXJD.export_excel(data, "data.xlsx")
  imported = INEXJD.import_excel("data.xlsx")
  ```
- **Cloud Storage Backends**: S3, Dropbox
- **Web Framework Plugins**: Flask, FastAPI, Django
- **Testing Helpers**: `INEXJDTestContext`, `setup_test_tables()`, `sample_test_data()`


### v1.6.0 - Security & Monitoring
- **Statistics & Analytics**:
  ```python
  print(INEXJD.get_usage_report())
  print(INEXJD.get_table_statistics("users"))
  ```
- **Data Compression**:
  ```python
  compressed = INEXJD.compress_data(data)
  decompressed = INEXJD.decompress_data(compressed)
  ```
- **Data Encryption**:
  ```python
  key = INEXJD.SimpleAES.generate_key()
  encrypted = INEXJD.SimpleAES.encrypt_data(data, key)
  decrypted = INEXJD.SimpleAES.decrypt_data(encrypted, key)
  ```
- **Audit Logging**:
  ```python
  INEXJD.log_action("users", "insert", {"count": 1})
  log_entries = INEXJD.get_audit_log("users")
  ```
- **Health Checks**:
  ```python
  print(INEXJD.run_diagnostics())
  print(INEXJD.is_database_healthy())
  ```


### v1.7.0 - Advanced Querying
- **Full-Text Search**:
  ```python
  results = INEXJD.full_text_search("products", "bluetooth")
  scored = INEXJD.search_with_scoring("products", "speaker")
  ```
- **Geospatial Queries**:
  ```python
  from INEXJD import haversine, find_nearby
  dist = haversine(48.8566, 2.3522, 51.5074, -0.1278)
  nearby = find_nearby("places", "lat", "lon", 48.8566, 2.3522, radius_km=1000)
  ```
- **Time Series Support**:
  ```python
  data = INEXJD.get_time_range("readings", "timestamp", start_time, end_time)
  resampled = INEXJD.resample_data("readings", "timestamp", "value", interval="day", agg="sum")
  ```
- **Relationships**:
  ```python
  INEXJD.define_relationship("customers", "id", "orders", "customer_id")
  customer = INEXJD.getTableData("customers")[0]
  orders = INEXJD.get_related_records("customers", customer, "orders")
  ```
- **WebSocket Real-time Sync**:
  ```python
  INEXJD.start_sync_server(host="localhost", port=8765)
  ```


## License
MIT
