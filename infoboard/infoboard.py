#!/usr/bin/env python
"""
infoboard application
This is the main infoboard apllication with both GUI and web interfaces.
"""

import os.path
from flask import render_template
from infoboard.weather import Weather
from infoboard.news import News
from infoboard.calendarfeed import CalendarFeed
from infoboard import app
from infoboard import settings

print(os.path.isfile("settings.json"))

LAT = settings.get_settings("WEATHER", "LAT")
LNG = settings.get_settings("WEATHER", "LNG")
LOC_ID = settings.get_settings("WEATHER", "LOC_ID")
CALENDAR_URL = settings.get_settings("CALENDAR", "SECRET_URL")
DISPLAY_CALENDAR = CalendarFeed(CALENDAR_URL)
HCAL = DISPLAY_CALENDAR.HtmlCalendar
print(HCAL)

LOCAL_WEATHER = Weather(LAT, LNG, LOC_ID)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title=settings.get_settings("DEFAULT", "WEB_TITLE"),
        weathercss=LOCAL_WEATHER.theme_css,
        weatherfont=LOCAL_WEATHER.font_css,
        weather=LOCAL_WEATHER.current_weather,
        weather_location=LOCAL_WEATHER.feed_location,
        news=News(3),
        htmlcalendar=HCAL
    )
