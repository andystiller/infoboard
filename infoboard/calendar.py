#!/usr/bin/env python
"""
Calendar module takes the event information from a calendar provider.
"""
import logging
from infoboard.providers.google_calendar import GoogleCalendar

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class CalendarFeed(object):
    """
    The CalendarFeed class handles getting the calendar from a provider,
    processing and outputting events
    """
    
    def __init__(self, calendar_path=''):

        LOGGER.info('Initialising calendar feed')
        self._weather_forecast = GoogleCalendar(calendar_path)

    def _theme_icons(self, icon):
        """
        Function to get the path to the required icon
        """
        LOGGER.info('Getting icon path')
        return DRIPICONS_PATH + DRIPICONS_SVG[icon] + '.svg'

    def _theme_icons_class(self, icon):
        """
        Function to get the path to the required icon
        """
        LOGGER.info('Getting icon class')
        return self.__THEME_PREFIX + DRIPICONS_SVG[icon]

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    calendar_feed = CalendarFeed()
    
if __name__ == "__main__":
    main()
