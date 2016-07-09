#!/usr/bin/python

from Tkinter import *
import requests
import os.path
from PIL import Image, ImageTk

import trello_connect
import omw_connect
import yle_connect


class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.weather["text"] = self.data.get_weather()
        self.weather["bg"] = "black"
        self.weather["fg"] = "white"
        self.weather["font"] = ("Helvetica Neue Light", 16, "normal")
        self.weather.pack({"side": "bottom"})

        self.news["text"] = self.data.get_news()
        self.news["bg"] = "black"
        self.news["fg"] = "white"
        self.news["font"] = ("Helvetica Neue Light", 16, "normal")
        self.news.pack({"side": "bottom"})

        self.todos["text"] = self.data.get_todos()
        self.todos["bg"] = "black"
        self.todos["fg"] = "white"
        self.todos["font"] = ("Helvetica Neue Light", 16, "normal")
        self.todos.pack({"side": "bottom"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.weather = Label(self)
        self.news = Label(self)
        self.todos = Label(self)
        self.pack()
        self.createWidgets()


weatherlogos = {}


def main():
    APPNAME = "JAMES"
    MF_WIDTH = 800
    MF_HEIGHT = 600

    win = Tk(baseName=APPNAME)
    win.wm_title(APPNAME)

    mf = Frame(win)
    mf.pack_propagate(False)

    mf.grid(row=0, column=0)

    cur_weather_f = Frame(mf)
    cur_weather_f.grid(row=1, column=0, sticky="W")
    weatherdata = omw_connect.get_weather()
    for r1 in range(0, len(weatherdata[0])):
        Label(cur_weather_f, text=weatherdata[0][r1],
              font=("Helvetica Neue", 12, "normal")) \
            .grid(row=r1, column=0, sticky=W)
    v_separator20 = Frame(mf, height=20)
    v_separator20.grid(row=2, column=0)

    weather_f = Frame(mf)
    weather_f.grid(row=3, column=0, sticky="W")
    for c in range(1,len(weatherdata)):
        for r in range(0,len(weatherdata[c])):
                Label(weather_f, text=weatherdata[c][r], font=("Helvetica Neue", 12, "normal"))\
                      .grid(row=r, column=c, sticky=W)
    v_separator50 = Frame(mf, height=50)
    v_separator50.grid(row=4, column=0)

    news_f = Frame(mf)
    news_f.grid(row=5, column=0, sticky="W")
    newsdata = yle_connect.get_headlines()
    for r in range(len(newsdata)):
        Label(news_f, text=newsdata[r], font=("Helvetica Neue", 12, "normal"))\
            .grid(row=r, column=1, sticky=W)

    #
    # for item in trello_connect.get_items():
    #     Label(text=item).pack()

    mainloop()


main()