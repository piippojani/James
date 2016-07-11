#!/usr/bin/python

import trolly
import threading


def get_items():
    #threading.Timer(7.0, get_items).start()
    TRELLO_APP_KEY = open('./conf/trello-apikey.txt', 'r').read().strip('\n')
    TRELLO_TOKEN =open('./conf/trello-token.txt', 'r').read().strip('\n')
    TRELLO_BOARD = open('./conf/trello-board.txt', 'r').read().strip('\n')
    client = trolly.client.Client(TRELLO_APP_KEY, TRELLO_TOKEN)
    print('Member: %s' % client.get_member())

    print('Organisations:')
    for organisation in client.get_organisations():
        print(' - %s' % organisation)

    print('Organisations:')
    for organisation in client.get_organisations():
        print(' - %s' % organisation)

    print('Boards:')
    for board in client.get_boards():
        print(' - %s' % board)

    print('Cards:')
    for card in client.get_cards():
        print(' - %s' % card)

    # Get all information from a card (works for boards, lists, etc. too):
    print('Detailed cards:')
    for card in client.get_cards(actions='all'):
        print(' - %s: %s' % (card, card.data))
    # trello = TrelloApi(TRELLO_APP_KEY)
    # trello.set_token(TRELLO_TOKEN)
    # lists = trello.boards.get_list(TRELLO_BOARD)
    # data = []
    # for list in lists:
    #     cards = trello.lists.get_card(list['id'])
    #     temp = []
    #     temp.append(list['name'])
    #     for card in cards:
    #         temp.append(card['name'])
    #     data.append(temp)
    return
