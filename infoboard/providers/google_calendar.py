#!/usr/bin/env python
"""
google_calendar module
This module downloads, caches and processes ical data from Google.
It uses their ical feed (either public or private).
"""

from datetime import datetime
from datetime import timedelta
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

class GoogleCalendar(object):  # added object base class for python2 compatibility.
    """
    The GoogleCalendar class handles getting, updating,
    itterating and processing calendars
    """
    __cache_folder = ""
    __TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.00'

    def __init__(self, calendar_path=''):
        LOGGER.info('Initialising Calendar')
        self._last_updated = None
        self._calendar_path = calendar_path
        self._file_loc = self.__cache_folder + 'calendar'  + '.ics'
        self.update_calendar()

    def _cache_valid(self):
        """
        Private function to check that the calendar is within 12 hours of the
        current date and time.
        Returns true is the cache is valid otherwise returns false.
        """
        LOGGER.info('Checking cache is valid')
        current_time = datetime.now()
        cache_is_valid = False

        LOGGER.info('Cache is valid: %s', cache_is_valid)
        return cache_is_valid

    def _download_ical(self):
        """
        Function to download the calendar from Google using the specifeid link.
        """
        pass

    def force_update(self):
        """
        Method to force an update fo the cached data and calendar
        """
        pass

    def update_calendar(self):
        """
        Method to get an updated calendar if available
        """
        pass

    def _load_calendar(self):
        """
        Function to load cached calendar
        """
        pass



def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    pass

if __name__ == "__main__":
    main()
