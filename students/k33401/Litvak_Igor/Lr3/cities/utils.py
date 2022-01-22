from math import sin, cos, sqrt, atan2, radians
from django.conf import settings
import requests


def get_external_api_response(lat: float, lon: float):
    """Get weather for lat and lon"""
    return requests.get(settings.EXTERNAL_API_BASE_URL, params={
        'appid': settings.EXTERNAL_API_KEY,
        'lat': lat,
        'lon': lon,
        'exclude': 'minutely,hourly,alerts',
        'units': 'metric'
    })


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    """Get distance between two points (not in km, but good for comparison)"""
    # Source: https://stackoverflow.com/a/63097060
    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return c
