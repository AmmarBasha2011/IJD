"""
INEX JSON Database - A JSON SQL-like Database Library

A lightweight library that provides SQL-like operations for JSON data storage.
Features:
- Simple JSON-based data storage
- SQL-like query operations
- Easy to use API for data manipulation
- No external database required
- Transactions with commit/rollback
- File locking for concurrency safety
- Indexing, caching, backup/restore, and more!
"""

from .functions.createFolder import createFolder
from .functions.getJsonContent import getJsonContent
from .functions.removeFile import removeFile
from .functions.writeJsonContent import writeJsonContent
from .SQL.aggregateTableData import aggregateTableData
from .SQL.deleteTableData import deleteTableData
from .SQL.copyTable import copyTable
from .SQL.insertTableData import insertTableData
from .SQL.validateTableData import validateTableData
from .SQL.countRecordsByCondition import countRecordsByCondition
from .SQL.countTableData import countTableData
from .SQL.createTable import createTable
from .SQL.deleteAllDataFromTable import deleteAllDataFromTable
from .SQL.deleteAllTables import deleteAllTables
from .SQL.deleteTable import deleteTable
from .SQL.deleteTableData import deleteTableData
from .SQL.duplicateTableData import duplicateTableData
from .SQL.exportTableData import exportTableData
from .SQL.filterRecords import filterRecords
from .SQL.getRecordById import getRecordById
from .SQL.getTableData import getTableData
from .SQL.getTables import getTables
from .SQL.getTableStructure import getTableStructure
from .SQL.importTableData import importTableData
from .SQL.insertTableData import insertTableData
from .SQL.listTableFields import listTableFields
from .SQL.mergeTablesData import mergeTablesData
from .SQL.renameTable import renameTable
from .SQL.restoreTableData import restoreTableData
from .SQL.searchTableData import searchTableData
from .SQL.setupAllThings import setupAllThings
from .SQL.sortTableData import sortTableData
from .SQL.updateMultipleRecords import updateMultipleRecords
from .SQL.updateSingleField import updateSingleField
from .SQL.updateTableData import updateTableData
from .SQL.updateTableStructure import updateTableStructure
from .SQL.validateTableData import validateTableData
from .SQL.transactions import begin_transaction, commit, rollback, is_transaction_active
from .SQL.indexing import create_index, drop_index, search_with_index, update_index, list_indexes
from .SQL.caching import cache_get, cache_put, cache_delete, cache_clear, cache_config
from .SQL.corruption_recovery import check_corruption, create_backup, recover_from_backup, auto_recover
from .SQL.backup_automation import enable_auto_backup, disable_auto_backup, backup_all_tables, list_backups, restore_from_latest_backup
from .functions.mmap_io import read_mmap_json, write_mmap_json
from .SQL.bulk_operations import bulk_insert, bulk_update, bulk_delete
from .SQL.distinct import get_distinct
from .SQL.orderby import sort_by_multiple
from .SQL.pagination import paginate, get_page_count
from .SQL.where_clause import filter_where
from .SQL.aggregation import aggregate
from .SQL.joins import join
from .SQL.subqueries import subquery_in, exists_subquery
from .SQL.schema_validation import define_table_schema, get_table_schema, validate_record, validate_and_insert, validate_table
from .SQL.migrations import get_current_version, set_current_version, create_migration, apply_migration, add_column, drop_column, rename_column, apply_pending_migrations, get_migration_history
from .functions.logger import get_logger, set_log_level
from .SQL.query_parser import parse_query, execute_query
from .SQL.model import Model
from .gui.app import run_gui
from .functions.io_formats import export_csv, import_csv, export_xml, import_xml, export_excel, import_excel
from .testing import INEXJDTestContext, pytest_fixture_inexjd_empty, setup_test_tables, sample_test_data
from .web_plugins import INEXJDFlask, create_inexjd_fastapi_router, INEXJDDjango
from .cloud_storage import CloudStorageBackend, S3Backend, DropboxBackend, GoogleDriveBackend, backup_to_cloud
from .SQL.statistics import get_table_statistics, get_database_statistics, get_usage_report
from .functions.data_protection import (
    compress_data, decompress_data, SimpleAES,
    save_compressed_table, load_compressed_table,
    save_encrypted_table, load_encrypted_table
)
from .SQL.audit import log_action, get_audit_log, clear_audit_log
from .health import check_file_integrity, run_diagnostics, is_database_healthy
setupAllThings()

__title__ = "INEXJD"
__license__ = "MIT"
__url__ = "https://github.com/AmmarBasha2011/IJD"
__uri__ = __url__
__doc__ = __doc__
__description__ = "A JSON SQL-like database library with statistics, compression, encryption, audit logging, health checks, and all previous features!"
__author__ = "International Technology For Everything"
__author_email__ = "ammarbasha2011@gmail.com"
__version__ = "1.6.0"
IJD = __version__
