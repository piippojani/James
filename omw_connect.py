#!/usr/bin/python

import json
import requests
import math
import time

DGR = u'\N{DEGREE SIGN}'


def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )


def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )


def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data


def get_weather():
    OWM_APP_KEY = open('./conf/owm-apikey.txt', 'r').read().strip('\n')
    #threading.Timer(9.0, get_weather).start()

    c = requests.get("http://api.openweathermap.org/data/2.5/weather?q=tampere,fi&units=metric&lang=fi&APPID="+OWM_APP_KEY)
    f = requests.get("http://api.openweathermap.org/data/2.5/forecast/city?q=tampere,fi&units=metric&lang=fi&APPID="+OWM_APP_KEY)
    current = json_loads_byteified(c.content)
    forecast = json_loads_byteified(f.content)
    i = 1
    data = []
    temp = [str(int(math.ceil(current["main"]["temp"])))+DGR+"C",
            current["weather"][0]["description"],
            ""]
    data.append(temp)
    for item in forecast["list"]:
        temp = [time.strftime("%H:%M", time.localtime(item["dt"])),
                str(int(math.ceil(item["main"]["temp"])))+DGR+"C",
                item["weather"][0]["description"]]
        data.append(temp)
        if i == 5:
            break
        else:
            i += 1
    return data
