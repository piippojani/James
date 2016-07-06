#!/usr/bin/python

import trello_connect
import omw_connect


def main():
    trello_connect.get_items()
    omw_connect.get_weather()

main()