#!/usr/bin/python

from trello import TrelloApi
import threading


def get_items():
    #threading.Timer(7.0, get_items).start()
    TRELLO_APP_KEY = open('./conf/api.txt', 'r').read().strip('\n')
    TRELLO_TOKEN =open('./conf/token.txt', 'r').read().strip('\n')
    TRELLO_BOARD = open('./conf/board.txt', 'r').read().strip('\n')
    trello = TrelloApi(TRELLO_APP_KEY)
    trello.set_token(TRELLO_TOKEN)
    lists = trello.boards.get_list(TRELLO_BOARD)
    data = []
    for list in lists:
        cards = trello.lists.get_card(list['id'])
        temp = []
        temp.append(list['name'])
        for card in cards:
            temp.append(card['name'])
        data.append(temp)
    return data
