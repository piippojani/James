#!/usr/bin/python

import trello_connect
import omw_connect
import yle_connect


def main():
    omw_connect.get_weather()
    yle_connect.get_headlines()
    trello_connect.get_items()


main()