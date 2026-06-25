import math
from ..functions.getJsonContent import getJsonContent


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance between two points on Earth (in km)!
    """
    R = 6371.0  # Earth radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R*c


def find_nearby(table_name, lat_field, lon_field, target_lat, target_lon, radius_km):
    """
    Find all records within radius_km of target coordinates!
    """
    data = getJsonContent(table_name)
    results = []
    for record in data:
        try:
            rec_lat = float(record.get(lat_field))
            rec_lon = float(record.get(lon_field))
        except (TypeError, ValueError):
            continue
        
        dist = haversine(target_lat, target_lon, rec_lat, rec_lon)
        if dist <= radius_km:
            results.append({"record": record, "distance_km": dist})
    results.sort(key=lambda x: x["distance_km"])
    return results
