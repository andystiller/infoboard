#!/usr/bin/env python
"""
Weather module takes the weather information in a weather provider
and displays the conditions for the current hour.
"""
from providers.metcheck_weather import MetcheckWeather

DRIPICONS_PATH = 'images/dripicons-weather/SVG/'
DRIPICONS = {
    # Sunny /Clear
    'SU' : 'sun.svg',
    'NSU' : 'moon-25.svg',
    # Fair
    'FA' : 'sun.svg',
    'NFA' : 'moon-25.svg',
    # Mostly Cloudy / Partly Cloudy
    'PC' : 'cloud-sun.svg',
    'NPC' : 'cloud-moon.svg',
    # Cloudy
    'CL' : 'clouds-sun.svg',
    'NCL' : 'clouds-moon.svg',
    # Mist/Fog
    'FG' : 'fog.svg',
    'NFG' : 'fog.svg',
    # Light Rain
    'LR' : 'cloud-rain-2-sun.svg',
    'NLR' : 'cloud-rain-2-moon.svg',
    # Sleet Showers
    'SL' : 'cloud-snow-sun.svg',
    'NSL' : 'cloud-snow-moon.svg',
    # Hazy/High Cloud
    'HZ' : 'cloud-fog-sun.svg',
    'NHZ' : 'cloud-fog-moon.svg',
    # ThunderSnow
    'TS' : 'cloud-rain-lightning-sun.svg',
    'NTS' : 'cloud-rain-lightning-moon.svg',
    # ThunderSleet
    'TL' : 'cloud-rain-lightning-moon.svg',
    'NTL' : 'cloud-rain-lightning-sun.svg',
    # Heavy Rain
    'HR' : 'cloud-rain-sun.svg',
    'NHR' : 'cloud-rain-moon.svg',
    # Intermittent Rain
    'RO' : 'cloud-rain-2-sun.svg',
    'NRO' : 'cloud-rain-2-sun.svg',
    # Drizzle
    'DZ' : 'cloud-drizzle-sun.svg',
    'NDZ' : 'cloud-drizzle-moon.svg',
    # Rain Showers
    'SH' : 'cloud-rain-2-sun.svg',
    'NSH' : 'cloud-rain-2-sun.svg',
    # Light Snow
    'LS' : 'cloud-snow-sun.svg',
    'NLS' : 'cloud-snow-moon.svg',
    # Light Sleet
    'LL' : 'cloud-snow-sun.svg',
    'NLL' : 'cloud-snow-moon.svg',
    # Heavy Snow
    'HS' : 'cloud-snow.svg',
    'NHS' : 'cloud-snow.svg',
    # Heavy Sleet
    'HL' : 'cloud-snow.svg',
    'NHL' : 'cloud-snow.svg',
    # Thunderstorms
    'TH' : 'cloud-rain-lightning-sun.sv',
    'NTH' : 'cloud-rain-lightning-moon.sv',
    # Wet & Windy
    'WW' : 'cloud-wind.svg',
    'NWW' : 'cloud-wind.svg',
    # Hail
    'HI' : 'cloud-hail-sun.svg',
    'NHI' : 'cloud-hail-moon.svg',
    # Snow Showers
    'SS' : 'cloud-snow-sun.svg',
    'NSS' : 'cloud-snow-moon.svg',
    # Dry & Windy
    'WI' : 'wind.svg',
    'NWI' : 'wind.svg',
    # Other icons
    'Precip' : 'umbrella.svg',
    'Temp' : 'thermometer-50.svg',
    'Wind' : 'wind.svg'
}

class Weather(object):
    """
    The Weather class handles gettin the forecast from a provider,
    processing and outputting forecasts
    """
    __THEME_FOLDER = ""

    def __init__(self, lat='51.5', lng='0.1', loc_id='57206'):
        self._weather_forecast = MetcheckWeather(lat, lng, loc_id)

    def _theme_icons(self, icon):
        """
        Function to get the path to the required icon
        """
        return DRIPICONS_PATH + DRIPICONS[icon]


    def _process_forecast(self, detailed_forecast):
        """
        Function to get only the require information from the forecast
        """
        forecast = {}
        forecast['Summary'] = detailed_forecast['iconName']
        forecast['Temperature'] = detailed_forecast['temperature'] + 'C'
        forecast['WindSpeed'] = detailed_forecast['windspeed'] + 'mph'
        forecast['WindDirection'] = detailed_forecast['windletter']
        forecast['ChanceOfRain'] = detailed_forecast['chanceofrain'] + '%'
        forecast['Cloud'] = detailed_forecast['totalcloud'] + '%'
        icon = self._theme_icons(detailed_forecast['icon'])
        forecast['Icon'] = icon
        return forecast

    def current_weather(self):
        """
        Function to get and theme the current weather forecast
        """
        return self._process_forecast(self._weather_forecast.current_weather)

    def next_hour(self):
        """
        Function to get and theme the weather forecast for the next hour
        """
        return = self._process_forecast(self._weather_forecast.next_hour)

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    weather_forecast = MetcheckWeather()
    print(weather_forecast.current_weather)
    print(weather_forecast.next_hour)

if __name__ == "__main__":
    main()
