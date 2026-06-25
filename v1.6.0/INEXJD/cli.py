#!/usr/bin/env python3
import argparse
import sys
import os
import json

# Add parent dir to path for local dev
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import INEXJD
from INEXJD.SQL.getTables import getTables
from INEXJD.SQL.query_parser import execute_query


def main():
    parser = argparse.ArgumentParser(description="INEXJD Command Line Interface")
    
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    
    # List tables
    list_parser = subparsers.add_parser("list", help="List all tables")
    
    # Query
    query_parser = subparsers.add_parser("query", help="Execute SQL-like query")
    query_parser.add_argument("query", nargs=argparse.REMAINDER, help="SQL-like query string")
    
    # Describe table
    desc_parser = subparsers.add_parser("desc", help="Describe table structure")
    desc_parser.add_argument("table", help="Table name")
    
    # Show table data
    show_parser = subparsers.add_parser("show", help="Show table data")
    show_parser.add_argument("table", help="Table name")
    
    # Version
    version_parser = subparsers.add_parser("version", help="Show INEXJD version")
    
    args = parser.parse_args()
    
    if args.command == "list":
        tables = getTables()
        print("Tables:")
        for table in tables.get("tables", {}):
            print(f"  - {table}")
    elif args.command == "query":
        query_str = " ".join(args.query)
        try:
            results = execute_query(query_str)
            print(json.dumps(results, indent=2))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    elif args.command == "desc":
        from INEXJD.SQL.getTableStructure import getTableStructure
        struct = getTableStructure(args.table)
        print(f"Table: {args.table}")
        print("Fields:", ", ".join(struct))
    elif args.command == "show":
        from INEXJD.SQL.getTableData import getTableData
        data = getTableData(args.table)
        print(json.dumps(data, indent=2))
    elif args.command == "version":
        print(f"INEXJD version {INEXJD.__version__}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
