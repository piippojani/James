#!/usr/bin/python

import trello_connect
import omw_connect
import yle_connect


def main():
    trello_connect.get_items()
    omw_connect.get_weather()
    yle_connect.get_headlines()

main()