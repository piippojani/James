#!/usr/bin/python

import json
import requests
import math

def get_weather():
    OWM_APP_KEY = open('./conf/owm-apikey.txt', 'r').read().strip('\n')
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast/city?q=tampere,fi&APPID="+OWM_APP_KEY)
    data = json.loads(r.content)
    i = 1
    print ""
    print "--- SÄÄENNUSTE ---"
    for item in data["list"]:
        print str(item["dt_txt"]) + " " + str(math.ceil(item["main"]["temp"]-273.15)) + " " + str(item["weather"][0]["description"])
        if i == 5:
            break
        else:
            i += 1
