#!/usr/bin/env python
"""
infoboard application
This is the main infoboard apllication with both GUI and web interfaces.
"""

from flask import render_template
from infoboard.weather import Weather
from infoboard.news import News
from infoboard import app

LOCAL_WEATHER = Weather(lat='51.5', lng='0.1', loc_id='57206')

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Infobard',
        weathercss=LOCAL_WEATHER.theme_css,
        weatherfont=LOCAL_WEATHER.font_css,
        weather=LOCAL_WEATHER.current_weather,
        news=News(3)
    )
