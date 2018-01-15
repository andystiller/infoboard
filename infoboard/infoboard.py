#!/usr/bin/env python
"""
infoboard application
This is the main infoboard apllication with both GUI and web interfaces.
"""

from flask import render_template
from infoboard.weather import Weather
from infoboard.news import News
from infoboard import app
from infoboard import settings

import os.path

print(os.path.isfile("settings.json"))

lat = settings.get_settings("WEATHER","LAT")
lng = settings.get_settings("WEATHER","LNG")
loc_id = settings.get_settings("WEATHER","LOC_ID")

LOCAL_WEATHER = Weather(lat, lng, loc_id)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title=settings.get_settings("DEFAULT","WEB_TITLE"),
        weathercss=LOCAL_WEATHER.theme_css,
        weatherfont=LOCAL_WEATHER.font_css,
        weather=LOCAL_WEATHER.current_weather,
        news=News(3)
    )
