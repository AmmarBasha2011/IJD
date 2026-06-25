import re
from ..functions.getJsonContent import getJsonContent


def full_text_search(table_name, query, fields=None, case_sensitive=False):
    """
    Perform full-text search on a table!
    """
    data = getJsonContent(table_name)
    if not fields:
        # Use all fields if none specified
        if not data:
            return []
        fields = list(data[0].keys())
    
    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(re.escape(query), flags)
    results = []

    for record in data:
        found = False
        for field in fields:
            val = str(record.get(field, ""))
            if pattern.search(val):
                found = True
                break
        if found:
            results.append(record)
    return results


def search_with_scoring(table_name, query, fields=None, case_sensitive=False):
    """
    Full-text search with simple scoring!
    """
    data = getJsonContent(table_name)
    if not fields:
        if not data:
            return []
        fields = list(data[0].keys())
    
    flags = 0 if case_sensitive else re.IGNORECASE
    query_terms = [t.lower() if not case_sensitive else t for t in query.split()]
    scored_results = []

    for record in data:
        score = 0
        for field in fields:
            val = str(record.get(field, "")).lower() if not case_sensitive else str(record.get(field, ""))
            for term in query_terms:
                if term in val:
                    score +=1
        if score > 0:
            scored_results.append({"record": record, "score": score})
    
    # Sort descending by score
    scored_results.sort(key=lambda x: -x["score"])
    return scored_results
