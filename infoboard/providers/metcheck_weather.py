#!/usr/bin/env python
"""
metcheck_weather module
This module downloads, caches and processes weather data from metcheck.com.
It uses their free json feed.
"""

from datetime import datetime
from datetime import timedelta
import logging
import json
import requests


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

class MetcheckWeather(object):  # added object base class for python2 compatibility.
    """
    The MetcheckWeather class handles getting, updating,
    itterating and processing forecasts
    """
    __cache_folder = ""
    __METCHECK_URL = 'http://ws1.metcheck.com/ENGINE/v9_0/json.asp'
    __TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.00'

    def __init__(self, lat='51.5', lng='0.1', loc_id='57206'):
        LOGGER.info('Initialising forecast')
        self._latlong = {'lat': lat, 'lon': lng, 'lid': loc_id}
        self._last_updated = None
        self._file_loc = self.__cache_folder + 'weather' + loc_id + '.json'
        self._feed_created = None
        self._feed_loaded = False
        self._forecast = {}
        LOGGER.debug('Forecast for location: %s', self._latlong)
        self.update_forecast()

    def _cache_valid(self):
        """
        Private function to check that the forecast is within 12 hours of the
        current date and for the correct location.
        Returns true is the cache is valid otherwise returns false.
        """
        LOGGER.info('Checking cache is valid')
        current_time = datetime.now()
        cache_is_valid = False

        LOGGER.debug('Last updated: %s', self._last_updated)
        #if self._last_updated != None and self._feed_created != None:
        if self._feed_created != None:
            valid_until = self._feed_created + timedelta(hours=12)
            LOGGER.debug('Feed created: %s', self._feed_created)
            LOGGER.debug('Feed loaded: %s', self._feed_loaded)
            LOGGER.debug('Feed valid until: %s', valid_until)
            LOGGER.debug('Current time: %s', current_time)
            #if current_time < valid_until and self._last_updated < current_time:
            if current_time < valid_until:
                #The cache is with 12 hours of current time
                cache_is_valid = True

        LOGGER.info('Cache is valid: %s', cache_is_valid)
        return cache_is_valid

    def _download_weather_data(self):
        """
        Function to download the weather data from metcheck.com for the
        specified lattitude and longitude and location ID.
        """
        LOGGER.info('Downloading weather data')
        url_params = self._latlong
        req = requests.get(self.__METCHECK_URL, params=url_params)
        LOGGER.debug('Request URL: %s', req.url)
        status_code = req.status_code
        LOGGER.debug('HTML status code: %d', status_code)

        # If we have recieved the forecast save it for later
        if status_code == 200:
            with open(self._file_loc, 'w', encoding='UTF-8') as json_data:
                chars_written = json_data.write(req.text)
                LOGGER.debug('Number of characters written: %d', chars_written)

                if chars_written == 0:
                    #if there is nothing written the file save failed
                    status_code = 999
        return status_code

    def force_update(self):
        """
        Method to force an update foe the cached data and forecast
        """
        LOGGER.info('Forcing Update')
        update_worked = False

        if self._download_weather_data() == 200:
            self._last_updated = datetime.now()
            update_worked = True

        LOGGER.debug('Updating worked: %s', update_worked)
        return update_worked

    def update_forecast(self):
        """
        Method to get an updated forecast if available
        """
        LOGGER.info('Updating weather forecast')
        if self._cache_valid():
            #Check that the cached version is valid
            LOGGER.info('update_forecast Cache is valid.')
        else:
            self.force_update()

        #if the feed isn't loaded try to load the cached version
        if self._feed_loaded is False:
            LOGGER.info('update_forecast: Feed loading')
            self._load_weather_json()
            LOGGER.debug('Feed loaded : %s', self._feed_loaded)

    def _load_weather_json(self):
        """
        Function to load cached weather data
        """
        LOGGER.info('Loading weather JSON')
        LOGGER.debug('File location: %s', self._file_loc)
        load_status = 'Not loaded'

        try:
            with open(self._file_loc, 'r', encoding='UTF-8') as json_data:
                weather_data = json.load(json_data)
                forecast_data = weather_data['metcheckData']['forecastLocation']['forecast']
                initial_run = weather_data['feedCreation']
                LOGGER.debug('Initial run data: %s', initial_run)
                self._feed_created = datetime.strptime(initial_run, self.__TIME_FORMAT)
                self._feed_loaded = True
                self._process_weather_json(forecast_data)
                load_status = 'Success'
        except IOError as file_error:
            load_status = str(file_error)
            #Need to add exception handling and file not found
        except json.JSONDecodeError as json_error:
            load_status = json_error.msg

        return load_status

    def _process_weather_json(self, forecast_data):
        """
        Function to processes the supplied json and converts it to a usable form
        """
        LOGGER.info('Processing weather data')
        for datavalue in forecast_data:
            forecast_time = datavalue['utcTime']
            self._forecast[forecast_time] = datavalue
            LOGGER.debug('Processing : %s', forecast_time)

    def _process_forecast(self, current_forecast):
        """ Function to remove unwanted items from the forecast
        """
        display_forecast = {}
        display_forecast['Chance of rain'] = current_forecast['chanceofrain']
        display_forecast['Rain'] = current_forecast['rain']
        display_forecast['Wind Speed'] = current_forecast['windspeed']
        display_forecast['Wind Direction'] = current_forecast['windletter']
        display_forecast['Description'] = current_forecast['iconName']
        display_forecast['Temperature'] = current_forecast['temperature']
        display_forecast['Cloud'] = current_forecast['totalcloud']
        display_forecast['Icon'] = current_forecast['icon']
        return display_forecast

    @property
    def current_weather(self):
        """ Property to get the current forecast
        """
        LOGGER.info('Get current weather')
        if self._feed_loaded is False:
            self.update_forecast() # update the forecast to download it if required and load it.

        current_time = datetime.now()
        time_to_check = current_time.replace(minute=0, second=0)
        LOGGER.debug('Time Format: %s', self.__TIME_FORMAT)
        LOGGER.debug('Time to fetch: %s', time_to_check.strftime(self.__TIME_FORMAT))
        current_forecast = self._forecast[time_to_check.strftime(self.__TIME_FORMAT)]
        LOGGER.debug('Forecast: %s', current_forecast)
        return self._process_forecast(current_forecast)

    @property
    def next_hour(self):
        """ Property to get the forecast for the next hour
        """
        LOGGER.info('Get next hour forecast')
        next_hour = datetime.now() + timedelta(hours=1)
        time_to_check = next_hour.replace(minute=0, second=0)
        current_forecast = self._forecast[time_to_check.strftime(self.__TIME_FORMAT)]
        return self._process_forecast(current_forecast)

    @property
    def feed_location(self):
        """ Property to return the feed location information
        """
        LOGGER.info('Get location of forecast')
        feed_location = 'None'

        if self._feed_created != None:
            try:
                with open(self._file_loc, 'r') as json_data:
                    weather_data = json.load(json_data)
                    feed_location = weather_data['metcheckData']['forecastLocation']['location']
            except IOError:
                pass
            except json.JSONDecodeError:
                pass

        return feed_location

    @property
    def credits(self):
        return '<a href="//www.metcheck.com/OTHER/ghx_global_hybrid_model.asp"><img src="//www.metcheck.com/IMAGES/LOGOS/ghx_poweredby.png" border=0></a>'


def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    weather_forecast = MetcheckWeather()
    print(weather_forecast.current_weather)
    print(weather_forecast.next_hour)

if __name__ == "__main__":
    main()
