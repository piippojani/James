#!/usr/bin/python

import trolly
import json


def get_items():
    TRELLO_APP_KEY = open('./conf/trello-apikey.txt', 'r').read().strip('\n')
    TRELLO_TOKEN =open('./conf/trello-token.txt', 'r').read().strip('\n')
    TRELLO_BOARD = open('./conf/trello-board.txt', 'r').read().strip('\n')
    client = trolly.client.Client(TRELLO_APP_KEY, TRELLO_TOKEN)
    data = []
    for card in client.get_board(TRELLO_BOARD).get_lists()[1].get_cards():
        card_info = card.get_card_information()
        temp = [card_info["name"], card_info["due"]]
        data.append(temp)
    return data
