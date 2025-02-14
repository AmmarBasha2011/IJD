"""
INEX JSON Database - A JSON SQL-like Database Library

A lightweight library that provides SQL-like operations for JSON data storage.
Features:
- Simple JSON-based data storage
- SQL-like query operations
- Easy to use API for data manipulation
- No external database required
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
setupAllThings()

__title__ = "INEXJD"
__license__ = "MIT"
__url__ = "https://github.com/AmmarBasha2011/IJD"
__uri__ = __url__
__doc__ = __doc__
__description__ = "A JSON SQL-like database library"
__author__ = "International Technology For Everything"
__author_email__ = "ammarbasha2011@gmail.com"
__version__ = "1.0.0rc4"
IJD = __version__
