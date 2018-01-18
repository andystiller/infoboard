#!/usr/bin/env python
"""
settings module
This module handles getting for all the other modules
"""
import json
import os.path

SETTINGS_FILE = "settings.json"
DEFAULT_SETTINGS = "default-settings.json"

def get_settings(section, key):
    """
    Function to get the required setting it tries to return
    the custom settings and if that fails it tries the 
    default settings if all fails it returns "". 
    """
    setting = ""
    
    if os.path.isfile(SETTINGS_FILE):
        print(SETTINGS_FILE)
        with open(SETTINGS_FILE, 'r') as configfile:
            config = json.load(configfile)
            setting = config[section][key]
    
    elif os.path.isfile(DEFAULT_SETTINGS):
        print(DEFAULT_SETTINGS)
        with open(DEFAULT_SETTINGS, 'r') as configfile:
            config = json.load(configfile)
            setting = config[section][key]

    return setting
