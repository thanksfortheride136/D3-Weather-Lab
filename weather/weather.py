# weather.py
# ------------
# By MWC Contributors
#
# Defines `print_weather`, which does all the work of fetching 
# the requested weather data and printing it out to the screen
# in a sensible way. 
# 
# It's your job to implement this function.

from weather.weather_apis import (
    geocode_location,
    estimate_location,
    get_weather_office,
    get_forecast
)

def print_weather(location=None, metric=False, verbose=False):
    """Prints out a weather report using the provided location, or using
    the user's current location if no location was provided. 
    When metric is True, prints out the weather in metric units.
    When verbose is True, prints out a more detailed report. 
    """
    print("Not finished...") # YOUR CODE HERE!
