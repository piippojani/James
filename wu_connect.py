#!/usr/bin/python

import json
import requests
import math
import time

DGR = u'\N{DEGREE SIGN}'


def get_weather():
    WU_API_KEY = open('./conf/wu-apikey.txt', 'r').read().strip('\n')
    #threading.Timer(9.0, get_weather).start()

    w = requests.get("http://api.wunderground.com/api/d1ddd1ca0c11d128/conditions/forecast/lang:FI/q/pws:IFINLAND22.json")
    weather = json.loads(w.text)
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
