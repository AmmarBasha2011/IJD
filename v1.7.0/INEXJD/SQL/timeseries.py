import datetime
from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent


def get_time_range(table_name, time_field, start_time, end_time):
    """
    Get all records between start_time and end_time!
    """
    data = getJsonContent(table_name)
    results = []
    for record in data:
        try:
            rec_time = datetime.datetime.fromisoformat(str(record.get(time_field)))
        except (TypeError, ValueError):
            continue
        if start_time <= rec_time <= end_time:
            results.append(record)
    # Sort by time ascending
    results.sort(key=lambda x: datetime.datetime.fromisoformat(str(x.get(time_field))))
    return results


def resample_data(table_name, time_field, value_field, interval="hour", agg="mean"):
    """
    Simple resampling of time-series data!
    """
    from collections import defaultdict
    data = getJsonContent(table_name)
    buckets = defaultdict(list)
    for record in data:
        try:
            rec_time = datetime.datetime.fromisoformat(str(record.get(time_field)))
            value = float(record.get(value_field))
        except (TypeError, ValueError):
            continue
        
        if interval == "hour":
            key = rec_time.replace(minute=0, second=0, microsecond=0)
        elif interval == "day":
            key = rec_time.replace(hour=0, minute=0, second=0, microsecond=0)
        elif interval == "week":
            key = (rec_time - datetime.timedelta(days=rec_time.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
        elif interval == "month":
            key = rec_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError(f"Unknown interval: {interval}")
        
        buckets[key].append(value)
    
    resampled = []
    agg_funcs = {
        "mean": lambda x: sum(x)/len(x),
        "sum": sum,
        "max": max,
        "min": min,
        "count": len
    }
    for bucket_time, values in sorted(buckets.items()):
        resampled.append({
            time_field: bucket_time.isoformat(),
            value_field: agg_funcs[agg](values)
        })
    return resampled
