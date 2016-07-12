#!/usr/bin/python

import json
import requests
import time
import html

DGR = u'\N{DEGREE SIGN}'
HIGH = u'\u25B4'
LOW = u'\u25BE'
RAIN = u'\u2602'
PERCENT = u'\u0025'
WEATHER_ICON = {
    "clear": u'\u2600',
    "cloudy": u'\u2601',
    "flurries": u'\u26C4',
    "fog": u'\u26C6',
    "hazy": u'\u26C6',
    "mostlycloudy": u'\u26C5',
    "mostlysunny": u'\u26C5',
    "partlycloudy": u'\u26C5',
    "partlysunny": u'\u26C5',
    "sleet": u'\u26C4',
    "rain": u'\u2614',
    "snow": u'\u26C7',
    "sunny": u'\u2600',
    "tstorms": u'\u2608',
    "unknown": u'\u2601',
    "chanceflurries": u'\u26C4',
    "chancerain": u'\u2614',
    "chancesleet": u'\u26C4',
    "chancesnow": u'\u26C7',
    "chancetstorms": u'\u2608'
}


def get_weather():
    WU_API_KEY = open('./conf/wu-apikey.txt', 'r').read().strip('\n')
    w = requests.get("http://api.wunderground.com/api/"+WU_API_KEY+"/conditions/hourly/forecast/lang:FI/q/pws:IFINLAND22.json")
    weather = json.loads(html.unescape(w.text))
    data = []
    temp = [WEATHER_ICON[weather["current_observation"]["icon"]] +
            str(int(weather["current_observation"]["temp_c"]))+DGR+"C",
            weather["current_observation"]["weather"],
            ""]
    data.append(temp)
    for i, item in enumerate(weather["forecast"]["simpleforecast"]["forecastday"]):
        temp = [str(item["date"]["day"])+"."+str(item["date"]["month"])+".",
                WEATHER_ICON[item["icon"]],
                HIGH+item["high"]["celsius"],
                LOW+item["low"]["celsius"],
                RAIN+" "+str(item["pop"])+PERCENT,
                item["conditions"]
                ]
        data.append(temp)
    return data
