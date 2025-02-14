# INEX JSON Database Library

INEX JSON Database Library (IJD) is a professional, project-grade JSON SQL-like database library designed to manage JSON-based data with ease and flexibility.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Installation
To install IJD, run:
```bash
pip install INEXJD
```
Alternatively, clone the repository and install locally:
```bash
git clone https://github.com/AmmarBasha2011/IJD.git
cd IJD
python setup.py install
```

## Usage

### Easy
```python
from IJD.SQL.createTable import createTable
print(createTable("users", []))
```

### Medium
```python
from IJD.SQL.insertTableData import insertTableData
result = insertTableData("users", {"id": 1, "name": "Alice"})
print(result)
```

### Hard
```python
from IJD.SQL.createTable import createTable
from IJD.SQL.insertTableData import insertTableData
result = createTable("orders", ["order_id", "user_id", "total"])
if result == "Table created successfully":
    result = insertTableData("orders", {"order_id": 555, "user_id": 1, "total": 99.99})
    if result == "Data inserted successfully":
        print("Order added successfully.")
    else:
        print(result)
else:
    print(result)
```

## License
This project is licensed under the MIT License.

## Contact
For inquiries or contributions, please contact:
- Name: International Technology For Everything
- Email: ammarbasha2011@gmail.com

## Module: IJD/SQL/createTable.py

This module provides the `createTable` function to create a new table in the JSON database.

#### Features
- Validates if the table already exists.
- Automatically creates the corresponding JSON file for the table.
- Updates the global "tables" metadata.

#### Best Practices
- Ensure table names are unique.
- Validate parameter types before calling.
- Check return values for proper error handling.

### Imports
- getJsonContent: Reads JSON data.
- writeJsonContent: Updates JSON files.

### Functionality
- Validates table uniqueness.
- Updates the global "tables" metadata.
- Creates an empty JSON file for the table.

### Returns
- "Table created successfully" on success.
- "Table already exists" if duplicate.

### Examples

#### Easy Example
```python
from IJD.SQL.createTable import createTable
print(createTable("users", []))
```

#### Medium Example
```python
from IJD.SQL.createTable import createTable
# Create a table with basic parameters
print(createTable("products", ["id", "name", "price"]))
```

#### High Example
```python
from IJD.SQL.createTable import createTable
# Advanced usage: create a table and execute further operations
result = createTable("orders", ["order_id", "user_id", "total"])
if result == "Table created successfully":
    # ...additional operations...
    print("Table 'orders' created. Proceed with further data insertion...")
else:
    print(result)
```

## Module: IJD/SQL/deleteAllDataFromTable.py

This module provides the `deleteAllDataFromTable` function to clear all data from a specified JSON table.

#### Features
- Efficiently resets the content of a table.
- Simplifies data cleanup operations.

#### Best Practices
- Confirm table existence before deleting.
- Backup data if necessary prior to deletion.

### Imports
- getJsonContent: Reads JSON data.
- writeJsonContent: Updates JSON files.

### Functionality
- Retrieves table content.
- Clears all data by writing an empty object.

### Returns
- "All data deleted from table successfully"

### Examples

#### Easy Example
```python
from IJD.SQL.deleteAllDataFromTable import deleteAllDataFromTable
print(deleteAllDataFromTable("users"))
```

#### Medium Example
```python
from IJD.SQL.deleteAllDataFromTable import deleteAllDataFromTable
# Delete all data from the 'products' table and print confirmation
result = deleteAllDataFromTable("products")
print(result)
```

#### High Example
```python
from IJD.SQL.deleteAllDataFromTable import deleteAllDataFromTable
# Advanced use-case: delete the table data and perform validation
result = deleteAllDataFromTable("orders")
if result == "All data deleted from table successfully":
    # ...additional operations...
    print("Data cleared from 'orders'. Ready for new entries.")
else:
    print(result)
```

## Module: IJD/SQL/deleteAllTables.py

This module provides the `deleteAllTables` function to remove all tables and reset the tables JSON file.

#### Features
- Iterates through all tables to delete related files.
- Resets the global "tables" metadata efficiently.

#### Best Practices
- Use with caution as it deletes all table data.
- Consider user confirmation before bulk deletion.

### Imports
- getJsonContent: Reads global table data.
- removeFile: Deletes table files.
- writeJsonContent: Writes updates back to the "tables" file.

### Functionality
- Iterates over each table to remove files.
- Resets the "tables" JSON file.

### Returns
- "All tables deleted successfully"

### Examples

#### Easy Example
```python
from IJD.SQL.deleteAllTables import deleteAllTables
print(deleteAllTables())
```

#### Medium Example
```python
from IJD.SQL.deleteAllTables import deleteAllTables
# Delete all tables and print confirmation
result = deleteAllTables()
print(result)
```

#### High Example
```python
from IJD.SQL.deleteAllTables import deleteAllTables
# Advanced use-case: delete all tables and perform additional cleanup
result = deleteAllTables()
if result == "All tables deleted successfully":
    # ...additional cleanup operations...
    print("Cleanup complete: all tables removed.")
else:
    print(result)
```

## Module: IJD/SQL/deleteTable.py

This module provides the `deleteTable` function to remove a specific table from the JSON database.

#### Features
- Checks for table existence before deletion.
- Updates the global table list after deletion.

#### Best Practices
- Validate table name input.
- Confirm deletion result for further actions.

### Imports
- getJsonContent: Reads JSON data.
- writeJsonContent: Updates JSON files.

### Functionality
- Checks for table existence.
- Deletes the table from the metadata.

### Returns
- "Table deleted successfully" on success.
- "Table not found" if the table does not exist.

### Examples

#### Easy Example
```python
from IJD.SQL.deleteTable import deleteTable
print(deleteTable("users"))
```

#### Medium Example
```python
from IJD.SQL.deleteTable import deleteTable
# Delete the 'products' table and print confirmation
result = deleteTable("products")
print(result)
```

#### High Example
```python
from IJD.SQL.deleteTable import deleteTable
# Advanced use-case: delete a table then check for its existence
result = deleteTable("orders")
if result == "Table deleted successfully":
    # ...additional operations...
    print("Table 'orders' successfully deleted.")
else:
    print(result)
```

## Module: IJD/SQL/deleteTableData.py

This module provides the `deleteTableData` function to remove a specific record from a table in the JSON database.

#### Features
- Accesses table structure to validate deletion.
- Efficiently removes record by index.

#### Best Practices
- Ensure the provided index is within range.
- Validate the table structure before deletion.

### Imports
- getTableStructure: Validates table schema.
- getJsonContent: Reads table data.
- writeJsonContent: Writes updates to JSON file.

### Functionality
- Retrieves table structure and JSON content.
- Deletes a record by index.

### Returns
- "Data deleted successfully" on success.
- "Table not found" if schema is invalid.

### Examples

#### Easy Example
```python
from IJD.SQL.deleteTableData import deleteTableData
print(deleteTableData("users", 0))
```

#### Medium Example
```python
from IJD.SQL.deleteTableData import deleteTableData
# Delete the first record from the 'products' table
result = deleteTableData("products", 0)
print(result)
```

#### High Example
```python
from IJD.SQL.deleteTableData import deleteTableData
# Advanced use-case: remove a record and perform further validation
result = deleteTableData("orders", 2)
if result == "Data deleted successfully":
    # ...additional operations...
    print("Record successfully removed from 'orders'.")
else:
    print(result)
```

## Module: IJD/SQL/getTableData.py

This module provides the `getTableData` function to retrieve the JSON content of a specified table.

#### Features
- Provides full table data as stored in a JSON file.
- Supports easy data retrieval for further processing.

#### Best Practices
- Handle empty results gracefully.
- Use proper error handling when processing output.

### Imports
- getJsonContent: Reads the table file.

### Functionality
- Returns full table data.

### Returns
- The JSON content of the table.

### Examples

#### Easy Example
```python
from IJD.SQL.getTableData import getTableData
print(getTableData("users"))
```

#### Medium Example
```python
from IJD.SQL.getTableData import getTableData
# Retrieve data from the 'products' table and print it
data = getTableData("products")
print(data)
```

#### High Example
```python
from IJD.SQL.getTableData import getTableData
# Advanced use-case: retrieve table data and process it further
data = getTableData("orders")
if data:
    # ...additional processing...
    print("Data retrieved:", data)
else:
    print("No data found.")
```

## Module: IJD/SQL/insertTableData.py

This module provides the `insertTableData` function to insert a new record into a specified table.

#### Features
- Verifies data fields against the table structure.
- Appends new records to the table with validation.

#### Best Practices
- Ensure provided data matches expected fields.
- Check operation results to verify insertion success.

### Imports
- getTableStructure: Validates the table schema.
- getJsonContent: Reads table data.
- writeJsonContent: Writes the updated record.

### Functionality
- Validates data against the table structure.
- Appends a new record to the table.

### Returns
- "Data inserted successfully" on success.

### Examples

#### Easy Example
```python
from IJD.SQL.insertTableData import insertTableData
print(insertTableData("users", {"id": 1, "name": "Alice"}))
```

#### Medium Example
```python
from IJD.SQL.insertTableData import insertTableData
# Insert a new record into the 'products' table
result = insertTableData("products", {"id": 101, "name": "Widget", "price": 19.99})
print(result)
```

#### High Example
```python
from IJD.SQL.insertTableData import insertTableData
# Advanced use-case: insert a record and perform further processing
result = insertTableData("orders", {"order_id": 555, "user_id": 1, "total": 99.99})
if result == "Data inserted successfully":
    # ...additional operations...
    print("Record added to 'orders'.")
else:
    print(result)
```

## Module: IJD/SQL/getTableStructure.py

This module provides the `getTableStructure` function to retrieve the structure of a specified table from the JSON store.

#### Features
- Returns the schema (field names) of a table.
- Distinguishes between valid tables and non-existent ones.

#### Best Practices
- Validate table names before usage.
- Handle error responses appropriately.

### Imports
- getJsonContent: Reads the "tables" JSON content.

### Functionality
- Checks if the table exists.
- Returns its structure if found.

### Returns
- A list of field names or "Table not found".

### Examples

#### Easy Example
```python
from IJD.SQL.getTableStructure import getTableStructure
print(getTableStructure("users"))
```

#### Medium Example
```python
from IJD.SQL.getTableStructure import getTableStructure
# Retrieve and print the structure of the 'products' table
structure = getTableStructure("products")
print(structure)
```

#### High Example
```python
from IJD.SQL.getTableStructure import getTableStructure
# Advanced use-case: validate table structure before further operations
structure = getTableStructure("orders")
if structure != "Table not found":
    # ...perform operations with valid structure...
    print("Table structure:", structure)
else:
    print("Error: Table not found.")
```

## Module: IJD/SQL/getTables.py

This module provides the `getTables` function to list all defined tables in the JSON database.

#### Features
- Retrieves a complete mapping of table names to structures.
- Supports dynamic listing of available tables.

#### Best Practices
- Use returned data for UI or debugging purposes.
- Validate the output to ensure data integrity.

### Imports
- getJsonContent: Reads the global "tables" file.

### Functionality
- Retrieves a dictionary mapping table names to their structures.

### Returns
- A dictionary of table names and structures.

### Examples

#### Easy Example
```python
from IJD.SQL.getTables import getTables
print(getTables())
```

#### Medium Example
```python
from IJD.SQL.getTables import getTables
# Retrieve tables and display the list of available tables
tables = getTables()
print("Available tables:", list(tables.keys()))
```

#### High Example
```python
from IJD.SQL.getTables import getTables
# Advanced use-case: retrieve tables and perform operations on each
tables = getTables()
for table, structure in tables.items():
    # ...additional operations...
    print(f"Table: {table}, Structure: {structure}")
```

## Module: IJD/SQL/updateTableStructure.py

This module provides the `updateTableStructure` function to update the structure (fields) of an existing table.

#### Features
- Updates both the metadata and the individual table file.
- Resets table data following a structure change.

#### Best Practices
- Confirm table existence prior to updating.
- Backup table data before altering the structure.

### Imports
- getJsonContent: Reads "tables" JSON.
- removeFile: Removes the existing table file.
- writeJsonContent: Writes changes to JSON files.

### Functionality
- Checks if the table exists.
- Resets the table data following schema changes.

### Returns
- "Table updated successfully" on success.
- "Table not found" if the table does not exist.

### Examples

#### Easy Example
```python
from IJD.SQL.updateTableStructure import updateTableStructure
print(updateTableStructure("users", ["id", "name", "email"]))
```

#### Medium Example
```python
from IJD.SQL.updateTableStructure import updateTableStructure
# Update the 'products' table structure and print confirmation
result = updateTableStructure("products", ["id", "name", "price", "stock"])
print(result)
```

#### High Example
```python
from IJD.SQL.updateTableStructure import updateTableStructure
# Advanced use-case: update table structure and trigger additional operations
result = updateTableStructure("orders", ["order_id", "user_id", "total", "date"])
if result == "Table updated successfully":
    # ...additional operations...
    print("Table structure for 'orders' updated. Ready for new data.")
else:
    print(result)
```

## Module: IJD/SQL/updateTableData.py

This module provides the `updateTableData` function to update a specific record in a table.

#### Features
- Validates new data against the current table structure.
- Modifies a record at a determined index.

#### Best Practices
- Ensure index is valid.
- Confirm that data keys exactly match the structure.

### Imports
- getTableStructure: Validates table structure.
- getJsonContent: Reads table data.
- writeJsonContent: Writes updated data.

### Functionality
- Validates record index and data fields.
- Updates the record at the given index.

### Returns
- "Data updated successfully" on success.
- Error message if data mismatch or table not found.

### Examples

#### Easy Example
```python
from IJD.SQL.updateTableData import updateTableData
print(updateTableData("users", {"id": 1, "name": "Alice Updated"}, 0))
```

#### Medium Example
```python
from IJD.SQL.updateTableData import updateTableData
# Update a record in the 'products' table and print confirmation
result = updateTableData("products", {"id": 101, "name": "Widget", "price": 17.99}, 0)
print(result)
```

#### High Example
```python
from IJD.SQL.updateTableData import updateTableData
# Advanced use-case: update table data and perform further validation
result = updateTableData("orders", {"order_id": 555, "user_id": 1, "total": 89.99, "date": "2023-10-01"}, 2)
if result == "Data updated successfully":
    # ...additional operations...
    print("Record in 'orders' updated successfully.")
else:
    print(result)
```

## Module: IJD/SQL/searchTableData.py

This module provides the `searchTableData` function to search for records in a table matching a query.

#### Features
- Filters records based on key-value query.
- Returns a list of matching records.

#### Best Practices
- Ensure the query keys exist in the table schema.
- Validate query values before calling.

### Imports
- getJsonContent: Reads table data.

### Functionality
- Filters records based on key-value matching.

### Returns
- A list of matching records.

### Examples

#### Easy Example
```python
from IJD.SQL.searchTableData import searchTableData
result = searchTableData("users", {"name": "Alice"})
print(result)
```

#### Medium Example
```python
from IJD.SQL.searchTableData import searchTableData
# Search for records with a specific field value
records = searchTableData("products", {"price": 19.99})
print(records)
```

#### High Example
```python
from IJD.SQL.searchTableData import searchTableData
# Advanced use-case: perform aggregations on search results
results = searchTableData("orders", {"status": "completed"})
if results:
    # ...additional processing...
    print("Completed orders:", results)
else:
    print("No matching records found.")
```

## Module: IJD/SQL/countTableData.py

This module provides the `countTableData` function to return the number of records in a table.

#### Features
- Counts records in the JSON-based table.
- Simple aggregation function.

#### Best Practices
- Confirm table data is loaded as a list.
- Use count results for pagination logic.

### Imports
- getJsonContent: Reads the table JSON data.

### Functionality
- Counts records from a JSON-based table.

### Returns
- Record count as an integer.

### Examples

#### Easy Example
```python
from IJD.SQL.countTableData import countTableData
print(countTableData("users"))
```

#### Medium Example
```python
from IJD.SQL.countTableData import countTableData
# Count records in 'products'
total = countTableData("products")
print("Total products:", total)
```

#### High Example
```python
from IJD.SQL.countTableData import countTableData
# Advanced use-case: use count for UI display
total = countTableData("orders")
if isinstance(total, int):
    print(f"There are {total} orders in the system.")
else:
    print(total)
```

## Module: IJD/SQL/sortTableData.py

This module provides the `sortTableData` function to sort table records by a specified key.

#### Features
- Sorts records in ascending or descending order.
- Writes sorted data back to the table file.

#### Best Practices
- Ensure the sort key exists in all records.
- Use error handling for inconsistent data types.

### Imports
- getJsonContent: Reads table data.
- writeJsonContent: Writes the sorted data.

### Functionality
- Sorts records in ascending or descending order.
- Updates the table file with sorted records.

### Returns
- "Data sorted successfully" on success.
- Error message if sorting fails.

### Examples

#### Easy Example
```python
from IJD.SQL.sortTableData import sortTableData
print(sortTableData("users", "id"))
```

#### Medium Example
```python
from IJD.SQL.sortTableData import sortTableData
# Sort 'products' by price in descending order
result = sortTableData("products", "price", reverse=True)
print(result)
```

#### High Example
```python
from IJD.SQL.sortTableData import sortTableData
# Advanced use-case: sort and then process sorted data
res = sortTableData("orders", "date")
if res == "Data sorted successfully":
    data = __import__('IJD.SQL.getTableData', fromlist=['getTableData']).getTableData("orders")
    # ...additional operations...
    print("Orders sorted by date")
else:
    print(res)
```

## Module: IJD/SQL/exportTableData.py

This module provides the `exportTableData` function to export table data to an external JSON file.

#### Features
- Exports complete table data to a specified file.
- Uses standard JSON format with indentations.

#### Best Practices
- Verify the file path is writable.
- Validate exported data for correctness.

### Imports
- getJsonContent: Reads table data.
- json module: For JSON file operations.

### Functionality
- Dumps table data into a specified JSON file with indentation.

### Returns
- "Data exported successfully" on success.
- Error message if export fails.

### Examples

#### Easy Example
```python
from IJD.SQL.exportTableData import exportTableData
print(exportTableData("users", "/path/to/export_users.json"))
```

#### Medium Example
```python
from IJD.SQL.exportTableData import exportTableData
# Export data from 'products'
result = exportTableData("products", "/path/to/export_products.json")
print(result)
```

#### High Example
```python
from IJD.SQL.exportTableData import exportTableData
# Advanced use-case: export then notify user
result = exportTableData("orders", "/path/to/export_orders.json")
if result == "Data exported successfully":
    # ...additional operations...
    print("Orders exported successfully.")
else:
    print(result)
```

## Module: IJD/SQL/importTableData.py

This module provides the `importTableData` function to import records from a JSON file into an existing table.

#### Features
- Merges imported records with existing table data.
- Validates that the imported file contains a list of records.

#### Best Practices
- Ensure the imported JSON file is properly formatted.
- Backup existing table data before importing.

### Imports
- getJsonContent: Reads table data.
- writeJsonContent: Writes updated table data.
- json module: For reading JSON from file.

### Functionality
- Reads and validates imported data.
- Merges imported records into the existing table.

### Returns
- "Data imported successfully" on success.
- Error message if import fails.

### Examples

#### Easy Example
```python
from IJD.SQL.importTableData import importTableData
print(importTableData("users", "/path/to/import_users.json"))
```

#### Medium Example
```python
from IJD.SQL.importTableData import importTableData
# Import records into 'products'
result = importTableData("products", "/path/to/import_products.json")
print(result)
```

#### High Example
```python
from IJD.SQL.importTableData import importTableData
# Advanced use-case: validate import operation and then process data
result = importTableData("orders", "/path/to/import_orders.json")
if result == "Data imported successfully":
    # ...additional operations...
    print("Orders imported and merged successfully.")
else:
    print(result)
```

## Module: IJD/SQL/updateSingleField.py

This module provides the `updateSingleField` function to update a single field in a record.

#### Features
- Updates just one field of a record.
- Validates index and field existence.

#### Best Practices
- Ensure the index is within range.
- Validate that the field exists before updating.

### Imports
- getJsonContent: Reads table data.
- writeJsonContent: Updates JSON file.

### Functionality
- Validates the record index and field existence.
- Updates the specified field with a new value.

### Returns
- "Field updated successfully" on success.
- Error message if index or field is invalid.

### Examples

#### Easy Example
```python
from IJD.SQL.updateSingleField import updateSingleField
print(updateSingleField("users", 0, "name", "Bob"))
```

#### Medium Example
```python
from IJD.SQL.updateSingleField import updateSingleField
result = updateSingleField("products", 2, "price", 29.99)
print(result)
```

#### High Example
```python
from IJD.SQL.updateSingleField import updateSingleField
# Advanced use: update and then proceed with further operations
result = updateSingleField("orders", 1, "status", "shipped")
if result == "Field updated successfully":
    # ...additional operations...
    print("Order status updated.")
else:
    print(result)
```

## Module: IJD/SQL/aggregateTableData.py

This module provides the `aggregateTableData` function to compute sum, count, and average for a numerical field.

#### Features
- Aggregates numerical data.
- Returns key statistical values.

#### Best Practices
- Ensure the specified field contains numeric values.
- Check for empty table data before aggregating.

### Imports
- getJsonContent: Reads table data.

### Functionality
- Filters numerical values from records.
- Computes aggregate metrics (sum, count, average).

### Returns
- A dictionary with keys: sum, count, average.
- Error message if field data is invalid.

### Examples

#### Easy Example
```python
from IJD.SQL.aggregateTableData import aggregateTableData
print(aggregateTableData("orders", "total"))
```

#### Medium Example
```python
from IJD.SQL.aggregateTableData import aggregateTableData
# Aggregate data in 'products' based on 'price'
stats = aggregateTableData("products", "price")
print(stats)
```

#### High Example
```python
from IJD.SQL.aggregateTableData import aggregateTableData
# Advanced use-case: using aggregate metrics for analytics
stats = aggregateTableData("sales", "amount")
if isinstance(stats, dict):
    print("Aggregated Data:", stats)
else:
    print(stats)
```

## Module: IJD/SQL/duplicateTableData.py

This module provides the `duplicateTableData` function to duplicate a record within a table.

#### Features
- Clones the record at a given index.
- Uses deep copy to prevent reference issues.

#### Best Practices
- Validate index boundaries.
- Ensure a duplicate is acceptable for your schema.

### Imports
- getJsonContent: Reads table data.
- writeJsonContent: Writes updated data.
- copy module: Performs deep copy of a record.

### Functionality
- Validates the record index.
- Appends a deep copy of the record to the table.

### Returns
- "Record duplicated successfully" on success.
- "Invalid index" if index is out-of-range.

### Examples

#### Easy Example
```python
from IJD.SQL.duplicateTableData import duplicateTableData
print(duplicateTableData("users", 0))
```

#### Medium Example
```python
from IJD.SQL.duplicateTableData import duplicateTableData
# Duplicate a record in 'products'
result = duplicateTableData("products", 1)
print(result)
```

#### High Example
```python
from IJD.SQL.duplicateTableData import duplicateTableData
# Advanced: duplicate a record and then log the updated table length
result = duplicateTableData("orders", 2)
if result == "Record duplicated successfully":
    # ...additional operations...
    print("Duplicate created.")
else:
    print(result)
```

## Module: IJD/SQL/mergeTablesData.py

This module provides the `mergeTablesData` function to merge data from a source table into a target table.

#### Features
- Combines records from two tables.
- Overwrites the target table with merged data.

#### Best Practices
- Ensure both tables have compatible data schemas.
- Backup target table before merging.

### Imports
- getJsonContent: Reads table data.
- writeJsonContent: Writes merged data.

### Functionality
- Retrieves data from both tables.
- Concatenates the source data to the target table.

### Returns
- "Tables merged successfully" on success.
- Error message if data is invalid.

### Examples

#### Easy Example
```python
from IJD.SQL.mergeTablesData import mergeTablesData
print(mergeTablesData("target", "source"))
```

#### Medium Example
```python
from IJD.SQL.mergeTablesData import mergeTablesData
# Merge 'archive' into 'orders'
result = mergeTablesData("orders", "archive")
print(result)
```

#### High Example
```python
from IJD.SQL.mergeTablesData import mergeTablesData
# Advanced: merge and then verify the update
result = mergeTablesData("products", "new_products")
if result == "Tables merged successfully":
    # ...additional operations...
    print("Products merged successfully.")
else:
    print(result)
```

## Module: IJD/SQL/filterRecords.py

This module provides the `filterRecords` function to filter records based on specified conditions.

#### Features
- Filters records that match all provided key-value conditions.
- Returns a list of matching records.

#### Best Practices
- Ensure condition keys exist in the record schema.
- Use for lightweight filtering purposes.

### Imports
- getJsonContent: Reads table data.

### Functionality
- Returns records that match all given key-value pairs.

### Returns
- A list of matching records.

### Examples

#### Easy Example
```python
from IJD.SQL.filterRecords import filterRecords
print(filterRecords("users", {"role": "admin"}))
```

#### Medium Example
```python
from IJD.SQL.filterRecords import filterRecords
# Filter products where category equals 'electronics'
results = filterRecords("products", {"category": "electronics"})
print(results)
```

#### High Example
```python
from IJD.SQL.filterRecords import filterRecords
# Advanced use-case: filter orders and handle empty result set
results = filterRecords("orders", {"status": "pending"})
if results:
    # ...additional processing...
    print("Pending orders:", results)
else:
    print("No pending orders found.")
```

## Module: IJD/SQL/renameTable.py

Provides the `renameTable` function to rename an existing table.

### Imports
- getJsonContent: Reads table metadata.
- writeJsonContent: Updates table metadata.
- os module: Renames the table file.

### Functionality
- Validates the existence of the old table and non-existence of the new table.
- Renames the table in metadata and renames its JSON file.

### Returns
- "Table renamed successfully" on success.
- Error message if conditions fail.

### Examples

#### Easy Example
```python
from IJD.SQL.renameTable import renameTable
print(renameTable("old_table", "new_table"))
```

## Module: IJD/SQL/copyTable.py

Provides the `copyTable` function to duplicate an existing table under a new name.

### Imports
- getJsonContent: Reads table metadata and data.
- writeJsonContent: Writes updated metadata and data.

### Functionality
- Checks for existence of the source table and non-existence of the destination.
- Copies schema and content from the source to the destination.

### Returns
- "Table copied successfully" on success.

### Examples

#### Easy Example
```python
from IJD.SQL.copyTable import copyTable
print(copyTable("products", "products_copy"))
```

## Module: IJD/SQL/backupTableData.py

Provides the `backupTableData` function to export table data into a backup JSON file.

### Imports
- getJsonContent: Reads table data.
- json module: Writes data to file.

### Functionality
- Dumps the content of a table to a specified backup file with indentation.

### Returns
- "Table backup created successfully" on success.
- Error message if backup fails.

### Examples

#### Easy Example
```python
from IJD.SQL.backupTableData import backupTableData
print(backupTableData("users", "/path/to/users_backup.json"))
```

## Module: IJD/SQL/restoreTableData.py

Provides the `restoreTableData` function to restore table data from a backup JSON file.

### Imports
- json module: Reads the backup file.
- writeJsonContent: Updates the table with restored data.

### Functionality
- Loads backup data from the file and writes it to the specified table.

### Returns
- "Table restored successfully" on success.
- Error message if restoration fails.

### Examples

#### Easy Example
```python
from IJD.SQL.restoreTableData import restoreTableData
print(restoreTableData("users", "/path/to/users_backup.json"))
```

## Module: IJD/SQL/updateMultipleRecords.py

Provides the `updateMultipleRecords` function to update all records matching a given condition.

### Imports
- getJsonContent: Reads table data.
- writeJsonContent: Writes updated table data.

### Functionality
- Iterates over each record and updates fields if conditions match.

### Returns
- "Records updated successfully" if at least one record was updated.
- "No matching records found" otherwise.

### Examples

#### Easy Example
```python
from IJD.SQL.updateMultipleRecords import updateMultipleRecords
print(updateMultipleRecords("orders", {"status": "pending"}, {"status": "approved"}))
```

## Module: IJD/SQL/getRecordById.py

Provides the `getRecordById` function to retrieve a record by its identifier.

### Imports
- getJsonContent: Reads table data.

### Functionality
- Searches for a record where the "id" field matches the provided value.

### Returns
- The matching record if found.
- "Record not found" otherwise.

### Examples

#### Easy Example
```python
from IJD.SQL.getRecordById import getRecordById
print(getRecordById("users", 101))
```

## Module: IJD/SQL/countRecordsByCondition.py

Provides the `countRecordsByCondition` function to count table records that meet a condition.

### Imports
- getJsonContent: Reads table data.

### Functionality
- Iterates over records and counts those matching all specified conditions.

### Returns
- An integer count of matching records.

### Examples

#### Easy Example
```python
from IJD.SQL.countRecordsByCondition import countRecordsByCondition
print(countRecordsByCondition("orders", {"status": "completed"}))
```

## Module: IJD/SQL/listTableFields.py

Provides the `listTableFields` function to list the field names of a table.

### Imports
- getTableStructure: Retrieves the table's schema.

### Functionality
- Returns the list of field names as defined in the table structure.

### Returns
- A list of fields on success or "Table not found" if invalid.

### Examples

#### Easy Example
```python
from IJD.SQL.listTableFields import listTableFields
print(listTableFields("users"))
```

## Module: IJD/SQL/validateTableData.py

Provides the `validateTableData` function to check data integrity against the table schema.

### Imports
- getJsonContent: Reads table data.
- getTableStructure: Retrieves table schema.

### Functionality
- Compares each record's keys with the table structure to ensure consistency.

### Returns
- "All records are valid" on success.
- "Invalid record format detected" if any record is mismatched.

### Examples

#### Easy Example
```python
from IJD.SQL.validateTableData import validateTableData
print(validateTableData("products"))
```

## Module: IJD/SQL/truncateTable.py

Provides the `truncateTable` function to remove all records from a table.

### Imports
- writeJsonContent: Writes data to the table file.

### Functionality
- Clears the table by writing an empty list to it.

### Returns
- "Table truncated successfully" on success.

### Examples

#### Easy Example
```python
from IJD.SQL.truncateTable import truncateTable
print(truncateTable("logs"))
```
