from functions.getJsonContent import getJsonContent

def aggregateTableData(table_name: str, field: str):
    """
    Aggregates numerical values of a specified field across all records.
    Returns sum, count, and average.
    """
    data = getJsonContent(table_name)
    if not isinstance(data, list) or not data:
        return "Table not found or empty"
    nums = [record.get(field) for record in data if isinstance(record.get(field), (int, float))]
    if not nums:
        return "Field does not contain numerical values"
    total = sum(nums)
    count = len(nums)
    average = total / count
    return {"sum": total, "count": count, "average": average}
