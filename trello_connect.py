#!/usr/bin/python

import json
from trello import TrelloApi


def get_board():
    TRELLO_APP_KEY = open('./conf/api.txt', 'r').read().strip('\n')
    TRELLO_TOKEN =open('./conf/token.txt', 'r').read().strip('\n')
    TRELLO_BOARD = open('./conf/board.txt', 'r').read().strip('\n')
    trello = TrelloApi(TRELLO_APP_KEY)
    trello.set_token(TRELLO_TOKEN)
    return trello.boards.get(TRELLO_BOARD)