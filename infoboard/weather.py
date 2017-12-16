#!/usr/bin/env python
"""
Weather module takes the weather information in a weather provider
and disaplays the conditions for the current hour.
"""
from providers.metcheck_weather import MetcheckWeather

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    weather_forecast = MetcheckWeather()
    print(weather_forecast.current_weather)
    print(weather_forecast.next_hour)

if __name__ == "__main__":
    main()