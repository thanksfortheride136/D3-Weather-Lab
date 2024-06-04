# weather_apis.py
# ---------------
# By MWC Contributors
#
# This module contains functions which interact with external APIs related to weather. 
# The module relies on USA-specific services; it will need to be extended using local 
# services for other regions.

# The National Weather Service (NWS) provides weather forecasting services across US
# states and territories. NWS divides the country into a grid of 2.5km squares, and 
# provides a forecast for each grid square. 
# 
# You will need to use these functions, but you don't need to edit this file.

import geocoder
import requests

def geocode_location(location_string):
    """Translates a location string into latitude and longitude coordinates.
    Uses the OpenStreetMap API. Returns a dict with keys 'lat' and 'lng' 
    as shown below. When no result is found, returns None.

        >>> geocode_location('11 Wall Street, New York')
        {"lat": -74.010865, "lng": 40.7071407}
    """
    result = geocoder.osm(location_string)
    if result:
        lat, lng = result.latlng
        return {'lat': lat, 'lng': lng}

def estimate_location(ip_address=None):
    """Estimates a location based on the request's IP address, returning
    latitude and longitude coodrdinates. When no IP address is provided, 
    uses the user's current IP address.

        >>> geocode_ip_address()
        {'lat': 23.6585116, 'lng': -102.0077097}
    """
    result = geocoder.ip(ip_address or 'me')
    if result:
        lat, lng = result.latlng
        return {'lat': lat, 'lng': lng}

def get_weather_office(lat, lng):
    """Looks up the NWS weather office for a pair of lat/lng coordinates.
    Returns a dict containing keys 'office', 'x', and 'y'.
    If no matching weather office is found, returns None.
        
        >>> coords = geocode_ip_address()
        >>> get_weather_office(coords['lat'], coords['lng'])
        {'office': 'BUF', 'x': 39, 'y': 59}
    """
    url = "https://api.weather.gov/points/{},{}".format(lat, lng)
    response = requests.get(url)
    if response.ok:
        result = response.json()
        return {
            "office": result['properties']['gridId'],
            "x": result['properties']['gridX'],
            'y': result['properties']['gridY']
        }

def get_forecast(office, x, y, metric=False):
    """Fetches the weather forecast for the given NWS office, and (x, y) NWS grid tile.
    Returns a list of time periods, where each time period is a dict containing keys
    as shown below. If no forecast can be found, returns None.
    When metric is True, returns temperatures in Celcius and wind speeds in km/hr.

    """
    url = "https://api.weather.gov/gridpoints/{}/{},{}/forecast".format(office, x, y)
    if metric: 
        url += "?units=si"
    response = requests.get(url)
    if response.ok:
        result = response.json()
        forecast = []
        for period in result['properties']['periods']:
            forecast.append({
                'name': period['name'],
                'temperature': period['temperature'],
                'wind_speed': period['windSpeed'],
                'wind_direction': period['windDirection'],
                'description': period['shortForecast'],
            })
        return forecast
