#!/usr/bin/env python
"""
infoboard application
This is the main infoboard apllication with both GUI and web interfaces.
"""

from flask import render_template
import infoboard.weather
from infoboard import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        weather=''
    )

