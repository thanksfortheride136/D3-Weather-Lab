# weather_cli.py
# ------------
# By MWC Contributors
#
# Defines a CLI (command-line interface) for weather. 
# This is the program that will actually run when you 
# run `weather` in Terminal. 
#
# You don't need to do anything with thie file.

from argparse import ArgumentParser
from weather.weather import print_weather

def weather_cli():
    """Provides a command-line interface for weather. 
    This function creates an ArgumentParser, which parses command line arguments.
    Then it calls `print_weather` with the provided arguments. 
    """
    parser = ArgumentParser("weather", description="Prints out a weather report")
    parser.add_argument("-l", "--location", help="Location for weather forecast")
    parser.add_argument("-m", "--metric", action="store_true", help="Use metric units")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    print_weather(location=args.location, metric=args.metric, verbose=args.verbose)

