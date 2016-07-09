#!/usr/bin/python

import json
import requests
import math
import threading

def get_weather():
    OWM_APP_KEY = open('./conf/owm-apikey.txt', 'r').read().strip('\n')
    #threading.Timer(9.0, get_weather).start()
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast/city?q=tampere,fi&APPID="+OWM_APP_KEY)
    content = json.loads(r.content)
    i = 1
    data = []
    for item in content["list"]:
        data.append(str(item["dt_txt"]) + " " + str(math.ceil(item["main"]["temp"]-273.15)) + " " +
                        str(item["weather"][0]["description"]))
        if i == 5:
            break
        else:
            i += 1
    return data
