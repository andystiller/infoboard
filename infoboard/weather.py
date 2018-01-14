#!/usr/bin/env python
"""
Weather module takes the weather information in a weather provider
and displays the conditions for the current hour.
"""
import logging
from infoboard.providers.metcheck_weather import MetcheckWeather

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEGREE_SIGN= u'\N{DEGREE SIGN}'
DRIPICONS_PATH = 'images/dripicons-weather/SVG/'
DRIPICONS_SVG = {
    # Sunny /Clear
    'SU' : 'sun',
    'NSU' : 'moon-25',
    # Fair
    'FA' : 'sun',
    'NFA' : 'moon-25',
    # Mostly Cloudy / Partly Cloudy
    'PC' : 'cloud-sun',
    'NPC' : 'cloud-moon',
    # Cloudy
    'CL' : 'clouds-sun',
    'NCL' : 'clouds-moon',
    # Mist/Fog
    'FG' : 'fog',
    'NFG' : 'fog',
    # Light Rain
    'LR' : 'cloud-rain-2-sun',
    'NLR' : 'cloud-rain-2-moon',
    # Sleet Showers
    'SL' : 'cloud-snow-sun',
    'NSL' : 'cloud-snow-moon',
    # Hazy/High Cloud
    'HZ' : 'cloud-fog-sun',
    'NHZ' : 'cloud-fog-moon',
    # ThunderSnow
    'TS' : 'cloud-rain-lightning-sun',
    'NTS' : 'cloud-rain-lightning-moon',
    # ThunderSleet
    'TL' : 'cloud-rain-lightning-moon',
    'NTL' : 'cloud-rain-lightning-sun',
    # Heavy Rain
    'HR' : 'cloud-rain-sun',
    'NHR' : 'cloud-rain-moon',
    # Intermittent Rain
    'RO' : 'cloud-rain-2-sun',
    'NRO' : 'cloud-rain-2-sun',
    # Drizzle
    'DZ' : 'cloud-drizzle-sun',
    'NDZ' : 'cloud-drizzle-moon',
    # Rain Showers
    'SH' : 'cloud-rain-2-sun',
    'NSH' : 'cloud-rain-2-sun',
    # Light Snow
    'LS' : 'cloud-snow-sun',
    'NLS' : 'cloud-snow-moon',
    # Light Sleet
    'LL' : 'cloud-snow-sun',
    'NLL' : 'cloud-snow-moon',
    # Heavy Snow
    'HS' : 'cloud-snow',
    'NHS' : 'cloud-snow',
    # Heavy Sleet
    'HL' : 'cloud-snow',
    'NHL' : 'cloud-snow',
    # Thunderstorms
    'TH' : 'cloud-rain-lightning-sun',
    'NTH' : 'cloud-rain-lightning-moon',
    # Wet & Windy
    'WW' : 'cloud-wind',
    'NWW' : 'cloud-wind',
    # Hail
    'HI' : 'cloud-hail-sun',
    'NHI' : 'cloud-hail-moon',
    # Snow Showers
    'SS' : 'cloud-snow-sun',
    'NSS' : 'cloud-snow-moon',
    # Dry & Windy
    'WI' : 'wind',
    'NWI' : 'wind',
    # Other icons
    'Precip' : 'umbrella',
    'Temp' : 'thermometer-50',
    'Wind' : 'wind'
}

class Weather(object):
    """
    The Weather class handles gettin the forecast from a provider,
    processing and outputting forecasts
    """
    __THEME_FOLDER = 'static\dripicons-weather'
    __THEME_PREFIX = 'diw-'

    def __init__(self, lat='51.5', lng='0.1', loc_id='57206'):

        logger.info('Initialising forecast')
        self._weather_forecast = MetcheckWeather(lat, lng, loc_id)

    def _theme_icons(self, icon):
        """
        Function to get the path to the required icon
        """

        logger.info('Getting icon path')
        return DRIPICONS_PATH + DRIPICONS_SVG[icon] + '.svg'

    def _theme_icons_class(self, icon):
        """
        Function to get the path to the required icon
        """
        logger.info('Getting icon class')
        return self.__THEME_PREFIX + DRIPICONS_SVG[icon]


    def _process_forecast(self, detailed_forecast):
        """
        Function to get only the require information from the forecast
        """
        logger.info('Processing forecast')
        forecast = {}
        logger.debug('Summary: %s', detailed_forecast)
        forecast['Summary'] = detailed_forecast['Description']
        forecast['Temperature'] = detailed_forecast['Temperature'] + DEGREE_SIGN + 'C'
        forecast['WindSpeed'] = detailed_forecast['Wind Speed'] + 'mph'
        forecast['WindDirection'] = detailed_forecast['Wind Direction']
        forecast['ChanceOfRain'] = detailed_forecast['Chance of rain'] + '%'
        forecast['Cloud'] = detailed_forecast['Cloud'] + '%'

        icon = self._theme_icons(detailed_forecast['Icon'])
        forecast['Icon'] = icon
        forecast['IconClass'] = self._theme_icons_class(detailed_forecast['Icon'])
        return forecast

    @property
    def theme_css(self):
        """
        Property to get the theme css URL
        """
        return self.__THEME_FOLDER + '\webfont\style.css'

    @property
    def font_css(self):
        """
        Property to get the font css URL
        """
        return self.__THEME_FOLDER + '\webfont\webfont.css'

    @property
    def current_weather(self):
        """
        Property to get and theme the current weather forecast
        """
        logger.info('Getting current forecast')
        _current_weather = self._weather_forecast.current_weather
        logger.debug('Summary: %s', _current_weather)
        return self._process_forecast(_current_weather)

    #@property
    #def next_hour(self):
    #    """
    #    Property to get and theme the weather forecast for the next hour
    #    """
    #    _nexthour = self._weather_forecast.next_hour
    #    return = self._process_forecast(_nexthour)

def main():
    """
    Entry point for testing if the file is run on it's own.
    """

    weather_forecast = Weather()
    print(weather_forecast.current_weather)

if __name__ == "__main__":
    main()
