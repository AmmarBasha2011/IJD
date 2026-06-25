from ..functions.getJsonContent import getJsonContent
from .where_clause import filter_where
from .distinct import get_distinct


def subquery_in(field, subquery_table, subquery_field, condition=None):
    """
    Get values from another table to use as an IN list.
    
    Args:
        field (str): Field to check in main table
        subquery_table (str): Table to get values from
        subquery_field (str): Field to take from subquery table
        condition (dict, optional): Condition to filter subquery
    
    Returns:
        list: Values from subquery
    """
    sub_data = getJsonContent(subquery_table)
    if condition:
        sub_data = filter_where(subquery_table, condition)
    return [r.get(subquery_field) for r in sub_data if r.get(subquery_field) is not None]


def exists_subquery(main_table, subquery_table, correlate):
    """
    Check if a correlated record exists in another table.
    
    Args:
        main_table (str): Main table
        subquery_table (str): Subquery table
        correlate (tuple): (main_field, sub_field) to correlate tables
    
    Returns:
        list: Records from main table where correlated subquery has matches
    """
    main_data = getJsonContent(main_table)
    sub_data = getJsonContent(subquery_table)
    main_field, sub_field = correlate
    
    sub_values = set(r.get(sub_field) for r in sub_data if r.get(sub_field) is not None)
    return [r for r in main_data if r.get(main_field) in sub_values]
