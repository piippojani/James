#!/usr/bin/python

import requests
import xml.etree.ElementTree as ET

def get_headlines():
    r = requests.get("http://yle.fi/uutiset/rss/paauutiset.rss")
    #print r.content
    root = ET.fromstring(str(r.content))
    i = 1
    print ""
    print "*** UUTISET ***"
    for item in root.iter("item"):
        print item[0].text
        if i == 10:
            break
        else:
            i += 1
