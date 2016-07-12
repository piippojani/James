#!/usr/bin/python

import json
import requests
import math
import time

DGR = u'\N{DEGREE SIGN}'

def get_weather():
    OWM_APP_KEY = open('./conf/owm-apikey.txt', 'r').read().strip('\n')

    c = requests.get("http://api.openweathermap.org/data/2.5/weather?q=tampere,fi&units=metric&lang=fi&APPID="+OWM_APP_KEY)
    f = requests.get("http://api.openweathermap.org/data/2.5/forecast/city?q=tampere,fi&units=metric&lang=fi&APPID="+OWM_APP_KEY)
    current = json.loads(c.text)
    forecast = json.loads(f.text)
    data = []
    temp = [str(int(math.ceil(current["main"]["temp"])))+DGR+"C",
            current["weather"][0]["description"],
            ""]
    data.append(temp)
    for i, item in enumerate(forecast["list"]):
        temp = [time.strftime("%H:%M", time.localtime(item["dt"])),
                str(int(math.ceil(item["main"]["temp"])))+DGR+"C",
                item["weather"][0]["description"]]
        data.append(temp)
        if i == 5:
            break
    return data
