#!/usr/bin/env python
"""
google_calendar module
This module downloads, caches and processes ical data from Google.
It uses their ical feed (either public or private).
"""

from datetime import datetime
from datetime import timedelta
import logging
import requests
import icalendar

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

class GoogleCalendar(object):  # added object base class for python2 compatibility.
    """
    The GoogleCalendar class handles getting, updating,
    itterating and processing calendars
    """
    __cache_folder = ""
    __TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.00'
    _file_loc = __cache_folder + 'calendar.ics'

    def __init__(self, calendar_path='', limit=5):
        LOGGER.info('Initialising Calendar')
        self._calendar_path = calendar_path
        self._ics_created = None
        self._ics_loaded = False
        self._gcal = None
        self._index = 0
        self._limit = limit
        self._iterator = None
        self.update_calendar()

    def _cache_valid(self):
        """
        Private function to check that the calendar is within 6 hours of the
        current date and time.
        Returns true is the cache is valid otherwise returns false.
        """
        LOGGER.info('Checking cache is valid')
        current_time = datetime.now()
        cache_is_valid = False

        if self._ics_created != None:
            valid_until = self._ics_created + timedelta(hours=6)
            LOGGER.debug('Calendar created: %s', self._ics_created)
            LOGGER.debug('Calendar loaded: %s', self._ics_loaded)
            LOGGER.debug('Calendar valid until: %s', valid_until)
            LOGGER.debug('Current time: %s', current_time)
            #if current_time < valid_until and self._last_updated < current_time:
            if current_time < valid_until:
                #The cache is with 12 hours of current time
                cache_is_valid = True

        LOGGER.info('Cache is valid: %s', cache_is_valid)
        return cache_is_valid

    def _download_ical(self):
        """
        Function to download the calendar from Google using the specifeid link.
        """
        if self._calendar_path == "":
            return 0

        LOGGER.info('Downloading calendar')
        req = requests.get(self._calendar_path)
        status_code = req.status_code
        LOGGER.debug('HTML status code: %d', status_code)

        # If we have recieved the forecast save it for later
        if status_code == 200:
            with open(self._file_loc, 'w', encoding='UTF-8') as ics_data:
                chars_written = ics_data.write(req.text)
                LOGGER.debug('Number of characters written: %d', chars_written)

                if chars_written == 0:
                    #if there is nothing written the file save failed
                    status_code = 999

        return status_code

    def force_update(self):
        """
        Method to force an update for the cached data and calendar
        """
        LOGGER.info('Forcing Update')
        update_worked = False

        if self._download_ical() == 200:
            update_worked = True

        LOGGER.debug('Updating worked: %s', update_worked)
        return update_worked

    def update_calendar(self):
        """
        Method to get an updated calendar if available
        """
        LOGGER.info('Updating calendar')

        if self._cache_valid():
            #Check that the cached version is valid
            LOGGER.info('update_calendar Cache is valid.')
        else:
            self.force_update()

        #if the calendar isn't loaded try to load the cached version
        if self._ics_loaded is False:
            LOGGER.info('update_calendar: Calendar loading')
            self._load_calendar()
            self._iterator = iter(self._gcal.walk('vevent'))
            LOGGER.debug('Calendar loaded : %s', self._ics_loaded)

    def _load_calendar(self):
        """
        Function to load cached calendar
        """
        with open(self._file_loc, 'r') as ics_data:
            self._gcal = icalendar.Calendar.from_ical(ics_data.read())
            self._ics_created = datetime.now()
            self._ics_loaded = True
            load_status = 'Success'

        return load_status

    def __iter__(self):
        return self

    def __next__(self):
        event = None

        if self._index < self._limit:
            raw_event = self._iterator.__next__()
            event = {}
            event['Description'] = raw_event['SUMMARY']
            event['Start'] = raw_event['DTSTART'].dt
            event['Location'] = raw_event['LOCATION']
            self._index += 1
        else:
            raise StopIteration

        return event


def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    pass

if __name__ == "__main__":
    main()
