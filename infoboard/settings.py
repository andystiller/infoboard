#!/usr/bin/env python
"""
settings module
This module handles getting for all the other modules
"""
import json
import os.path

SETTINGS_FILE ="settings.json"
DEFAULT_SETTINGS ="default-settings.json"

def get_settings(section, key):
    setting = ""

    if os.path.isfile(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            config = json.load(f)
        
        setting = config[section][key]

    elif os.path.isfile(DEFAULT_SETTINGS):
        with open(DEFAULT_SETTINGS, 'r') as f:
            config = json.load(f)
        
        setting = config[section][key]

    return setting