#!/usr/bin/env python
"""
Weather module takes the weather information in a weather provider
and displays the conditions for the current hour.
"""
from providers.metcheck_weather import MetcheckWeather

dripicons_path = 'images/dripicons-weather/SVG'
dripicons = {
        # Sunny /Clear
        'SU' : 'sun.svg',
        'NSU' : 'moon-25.svg',
        # Fair
        'FA' : 'sun.svg',
        'NFA' : 'moon-25.svg',
        # Mostly Cloudy
        'PC' : 'cloud-sun.svg',
        'NPC' : 'cloud-moon.svg',
        # Cloudy
        'CL' : 'clouds-sun.svg',
        'NCL' : 'clouds-moon.svg',
        # Mist/Fog
        'FG' : 'fog.svg',
        'NFG' : 'fog.svg',
        # Light Rain
        'LR' : 'cloud-rain-2-sun.svg',
        'NLR' : 'cloud-rain-2-moon.svg',
        # Sleet Showers
        'SL' : 'cloud-snow-sun.svg',
        'NSL' : 'cloud-snow-moon.svg',
        # Hazy/High Cloud
        'HZ' : 'cloud-fog-sun.svg',
        'NHZ' : 'cloud-fog-moon.svg',
        # ThunderSnow
        'TS' : 'cloud-rain-lightning-sun.svg',
        'NTS' : 'cloud-rain-lightning-moon.svg',
        # ThunderSleet
        'TL' : 'cloud-rain-lightning-moon.svg',
        'NTL' : 'cloud-rain-lightning-sun.svg',
        # Heavy Rain
        'HR' : 'cloud-rain-sun.svg',
        'NHR' : 'cloud-rain-moon.svg',
        # Intermittent Rain
        'RO' : 'cloud-rain-2-sun.svg',
        'NRO' : 'cloud-rain-2-sun.svg',
        # Drizzle
        'DZ' : 'cloud-drizzle-sun.svg',
        'NDZ' : 'cloud-drizzle-moon.svg',
        # Rain Showers
        'SH' : 'cloud-rain-2-sun.svg',
        'NSH' : 'cloud-rain-2-sun.svg',
        # Light Snow
        'LS' : 'cloud-snow-sun.svg',
        'NLS' : 'cloud-snow-moon.svg',
        # Light Sleet
        'LL' : 'cloud-snow-sun.svg',
        'NLL' : 'cloud-snow-moon.svg',
        # Heavy Snow
        'HS' : 'cloud-snow.svg',
        'NHS' : 'cloud-snow.svg',
        # Heavy Sleet
        'HL' : 'cloud-snow.svg',
        'NHL' : 'cloud-snow.svg',
        # Thunderstorms
        'TH' : 'cloud-rain-lightning-sun.sv',
        'NTH' : 'cloud-rain-lightning-moon.sv',
        # Wet & Windy
        'WW' : 'cloud-wind.svg',
        'NWW' : 'cloud-wind.svg',
        #Partly Cloudy
        'PC' : 'cloud-sun.svg',
        'NPC' : 'cloud-moon.svg',
        # Hail
        'HI' : 'cloud-hail-sun.svg',
        'NHI' : 'cloud-hail-moon.svg',
        # Snow Showers
        'SS' : 'cloud-snow-sun.svg',
        'NSS' : 'cloud-snow-moon.svg',
        # Dry & Windy
        'WI' : 'wind.svg',
        'NWI' : 'wind.svg',
        # Other icons
        'Precip' : 'umbrella.svg',
        'Temp' : 'thermometer-50.svg',
        'Wind' : 'wind.svg'
}

def main():
    """
    Entry point for testing if the file is run on it's own.
    """
    weather_forecast = MetcheckWeather()
    print(weather_forecast.current_weather)
    print(weather_forecast.next_hour)

if __name__ == "__main__":
    main()