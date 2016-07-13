#!/usr/bin/python

import requests
import xml.etree.ElementTree as ET

LIMIT = 4

def get_length():
    return LIMIT

def get_headlines():
    r = requests.get("http://yle.fi/uutiset/rss/paauutiset.rss")
    root = ET.fromstring(r.text)
    data = []
    for i, item in enumerate(root.iter("item")):
        data.append(item[0].text)
        if i == LIMIT:
            break
    return data