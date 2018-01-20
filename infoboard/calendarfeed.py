#!/usr/bin/env python
"""
Calendar module takes the event information from a calendar provider.
"""
import logging
import calendar
from datetime import datetime
from infoboard.providers.google_calendar import GoogleCalendar

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class CalendarFeed(object):
    """
    The CalendarFeed class handles getting the calendar from a provider,
    processing and outputting events
    """

    def __init__(self, calendar_path='', limit=5):

        LOGGER.info('Initialising calendar feed')
        self._limit = limit
        self._index = 0
        self._gcal = GoogleCalendar(calendar_path)



    @property
    def htmlcalendar(self):
        """
        Generates an HTML month calendar
        """
        now = datetime.now()
        html_calendar = calendar.HTMLCalendar()
        output = html_calendar.formatmonth(now.year, now.month)
        return output

    def __iter__(self):
        return self

    def __next__(self):
        event = None

        if self._index < self._limit:
            event = self._gcal.__next__()
            LOGGER.debug('Event: %s', event)
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
