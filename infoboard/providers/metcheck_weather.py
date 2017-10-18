"""
metcheck_weather module
This module downloads, caches and processes weather data from metcheck.com.
It uses their free json feed.
"""

from datetime import datetime
from datetime import timedelta
import json
import requests


class Forecast(object):  # added object base class for python2 compatibility.
    """
    The Forecast class handles getting, updating,
    itterating and processing forecasts
    """
    __cache_folder = ""
    __METCHECK_URL = 'http://ws1.metcheck.com/ENGINE/v9_0/json.asp'
    __TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.00'

    def __init__(self, lat='51.5', lng='0.1', loc_id='57206'):
        self._lat = lat
        self._long = lng
        self._loc_id = loc_id
        self._last_updated = None
        self._file_loc = self.__cache_folder + 'weather' + self._loc_id + '.json'
        self._feed_created = None
        self._feed_location = None
        self._feed_loaded = False
        self._forecast = {}

        self.update_forecast()

    def _cache_valid(self):
        """
        Private function to check that the forecast is within 12 hours of the
        current date and for the correct location.
        Returns true is the cache is valid otherwise returns false.
        """
        current_time = datetime.now()
        cache_is_valid = False

        print(self._last_updated)
        #if self._last_updated != None and self._feed_created != None:
        if self._feed_created != None:
            valid_until = self._feed_created + timedelta(hours=12)
            print(self._feed_created)
            print(valid_until)
            print(current_time)
            #if current_time < valid_until and self._last_updated < current_time:
            if current_time < valid_until:
                #The cache is with 12 hours of current time
                cache_is_valid = True
                print('Cache is valid')

        return cache_is_valid

    def _download_weather_data(self):
        """
        Function to download the weather data from metcheck.com for the
        specified lattitude and longitude and location ID.
        """
        url_params = {'lat': self._lat, 'lon': self._long, 'lid': self._loc_id}
        req = requests.get(self.__METCHECK_URL, params=url_params)
        print(req.url)
        status_code = req.status_code
        print(status_code)

        # If we have recieved the forecast save it for later
        if status_code == 200:
            with open(self._file_loc, 'w') as json_data:
                chars_written = json_data.write(req.text)
                print(chars_written)

                if (chars_written == 0):
                    #if there is nothing written the file save failed
                    status_code = 999
        return status_code

    def force_update(self):
        """
        Method to force an update fo teh cached data and forecast
        """
        update_worked = False

        if (self._download_weather_data() == 200):
            self._last_updated = datetime.now()
            update_worked = True

        return update_worked

    def update_forecast(self):
        """
        Method to get an updated forecast if available
        """
        #if the feed isn't loaded try to load the cached version
        if self._feed_loaded is False:
            print('update_forecast: Feed loading')
            self._load_weather_json()
            print(self._feed_loaded)

        if self._cache_valid():
            #Check that the cached version is valid
            print('update_forecast Cache is valid.')
        else:
            self.force_update()

    def _load_weather_json(self):
        """
        Function to load cached weather data
        """
        print(self._file_loc)
        load_status = 'Not loaded'

        try:
            with open(self._file_loc, 'r') as json_data:
                weather_data = json.load(json_data)
                forecast_data = weather_data['metcheckData']['forecastLocation']['forecast']
                initial_run = weather_data['feedCreation']
                print(initial_run)
                self._feed_created = datetime.strptime(initial_run, self.__TIME_FORMAT)
                self._feed_location = weather_data['metcheckData']['forecastLocation']['location']
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
        for datavalue in forecast_data:
            forecast_time = datavalue['utcTime']
            self._forecast[forecast_time] = datavalue
            print(forecast_time)

    @property
    def current_weather(self):
        """ Property to get the current forecast
        """
        current_time = datetime.now()
        time_to_check = current_time.replace(minute=0, second=0)
        return self._forecast[time_to_check.strftime(self.__TIME_FORMAT)]

    @property
    def next_hour(self):
        """ Property to get the forecast for the next hour
        """
        next_hour = datetime.now() + timedelta(hours=1)
        time_to_check = next_hour.replace(minute=0, second=0)
        return self._forecast[time_to_check.strftime(self.__TIME_FORMAT)]


def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    weather_forecast = Forecast()
    print(weather_forecast.current_weather)
    print(weather_forecast.next_hour)

if __name__ == "__main__":
    main()
