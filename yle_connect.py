#!/usr/bin/python

import requests
import xml.etree.ElementTree as ET
import threading

def get_headlines():
    #threading.Timer(5.0, get_headlines).start()
    r = requests.get("http://yle.fi/uutiset/rss/paauutiset.rss")
    #print r.content
    root = ET.fromstring(str(r.content))
    i = 1
    data = []
    for item in root.iter("item"):
        data.append(item[0].text)
        if i == 5:
            break
        else:
            i += 1
    return data