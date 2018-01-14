#!/usr/bin/env python
"""
infoboard application
This is the main infoboard apllication with both GUI and web interfaces.
"""

from flask import render_template
from infoboard.weather import Weather
from infoboard import app

local_weather = Weather(lat='51.5', lng='0.1', loc_id='57206')

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Infobard',
        weathercss=local_weather.theme_css,
        weatherfont=local_weather.font_css,
        weather=local_weather.current_weather
    )
