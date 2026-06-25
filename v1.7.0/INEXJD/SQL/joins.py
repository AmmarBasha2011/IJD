from ..functions.getJsonContent import getJsonContent


def join(table1, table2, join_type, on_condition):
    """
    Join two tables using specified join type and condition.
    
    Args:
        table1 (str): First table name
        table2 (str): Second table name
        join_type (str): "INNER", "LEFT", "RIGHT", "FULL"
        on_condition (tuple): (field1, field2)
    
    Returns:
        list: Joined records
    """
    data1 = getJsonContent(table1)
    data2 = getJsonContent(table2)
    field1, field2 = on_condition
    joined = []
    
    if join_type == "INNER":
        for r1 in data1:
            for r2 in data2:
                if r1.get(field1) == r2.get(field2):
                    merged = {f"{table1}.{k}": v for k, v in r1.items()}
                    merged.update({f"{table2}.{k}": v for k, v in r2.items()})
                    joined.append(merged)
    elif join_type == "LEFT":
        for r1 in data1:
            match_found = False
            for r2 in data2:
                if r1.get(field1) == r2.get(field2):
                    merged = {f"{table1}.{k}": v for k, v in r1.items()}
                    merged.update({f"{table2}.{k}": v for k, v in r2.items()})
                    joined.append(merged)
                    match_found = True
            if not match_found:
                merged = {f"{table1}.{k}": v for k, v in r1.items()}
                for k in data2[0].keys() if data2 else []:
                    merged[f"{table2}.{k}"] = None
                joined.append(merged)
    elif join_type == "RIGHT":
        for r2 in data2:
            match_found = False
            for r1 in data1:
                if r1.get(field1) == r2.get(field2):
                    merged = {f"{table1}.{k}": v for k, v in r1.items()}
                    merged.update({f"{table2}.{k}": v for k, v in r2.items()})
                    joined.append(merged)
                    match_found = True
            if not match_found:
                merged = {f"{table2}.{k}": v for k, v in r2.items()}
                for k in data1[0].keys() if data1 else []:
                    merged[f"{table1}.{k}"] = None
                joined.append(merged)
    elif join_type == "FULL":
        # First left join
        left_part = join(table1, table2, "LEFT", on_condition)
        # Then find right-only and add
        right_keys = set()
        for r in left_part:
            key = r.get(f"{table2}.{field2}")
            if key is not None:
                right_keys.add(key)
        for r2 in data2:
            if r2.get(field2) not in right_keys:
                merged = {f"{table2}.{k}": v for k, v in r2.items()}
                for k in data1[0].keys() if data1 else []:
                    merged[f"{table1}.{k}"] = None
                left_part.append(merged)
        return left_part
    
    return joined
