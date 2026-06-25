from ..functions.getJsonContent import getJsonContent


def paginate(table_name, limit, offset=0):
    """
    Get a paginated subset of table data.
    
    Args:
        table_name (str): Target table
        limit (int): Maximum records to return
        offset (int, optional): Number of records to skip
    
    Returns:
        list: Paginated records
    """
    table_data = getJsonContent(table_name)
    return table_data[offset:offset+limit]


def get_page_count(table_name, page_size):
    """
    Get total number of pages for a given page size.
    
    Args:
        table_name (str): Target table
        page_size (int): Number of records per page
    
    Returns:
        int: Total pages
    """
    table_data = getJsonContent(table_name)
    total = len(table_data)
    return (total + page_size - 1) // page_size
