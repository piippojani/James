#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import requests
import os.path
from PIL import Image, ImageTk
import time

import trello_connect
import omw_connect
import yle_connect


def main():
    APPNAME = "JAMES"
    MF_WIDTH = 800
    MF_HEIGHT = 600
    SMALLFONT = 14
    MEDIUMFONT = 20
    LARGEFONT = 60

    win = Tk(baseName=APPNAME)
    win.wm_title(APPNAME)

    mf = Frame(win)
    mf.pack_propagate(False)

    mf.grid(row=0, column=0)

    cur_weather_f = Frame(mf)
    cur_weather_f.grid(row=0, column=0, sticky="NW")

    weatherdata = omw_connect.get_weather()
    for r1 in range(0, len(weatherdata[0])):
        fontsize = MEDIUMFONT
        if r1 == 0:
            fontsize = LARGEFONT
        Label(cur_weather_f, text=weatherdata[0][r1],
              font=("Helvetica Neue Light", fontsize, "normal")) \
            .grid(row=r1, column=0, sticky=W)

    v_separator20 = Frame(mf, height=20)
    v_separator20.grid(row=1, column=0)

    weather_f = Frame(mf)
    weather_f.grid(row=2, column=0, sticky="W")
    for c in range(1,len(weatherdata)):
        for r in range(0,len(weatherdata[c])):
            Label(weather_f, text=weatherdata[c][r], font=("Helvetica Neue Light", SMALLFONT, "normal"))\
                  .grid(row=c, column=r, sticky=W)

    v_separator50 = Frame(mf, height=50)
    v_separator50.grid(row=3, column=0)

    news_f = Frame(mf)
    news_f.grid(row=4, column=0, sticky="W")
    newsdata = yle_connect.get_headlines()
    for r in range(len(newsdata)):
        Label(news_f, text=newsdata[r], font=("Helvetica Neue Light", SMALLFONT, "normal"))\
            .grid(row=r, column=1, sticky=W)

    h_separator100 = Frame(mf, width=100)
    h_separator100.grid(row=0, column=1)

    clock_f = Frame(mf)
    clock_f.grid(row=0, column=2, sticky=N)

    clock = Label(clock_f, font=("Helvetica Neue Light", LARGEFONT, "normal"))
    clock.grid(row=0, column=1, sticky=E)

    date = Label(clock_f, font=("Helvetica Neue Light", MEDIUMFONT, "normal"))
    date.grid(row=1, column=0, sticky=E, columnspan=2)

    def tick():
        # if time string has changed, update it
        weekday = {
            "0" : "Sunnuntai",
            "1" : "Maanantai",
            "2" : "Tiistai",
            "3" : "Keskiviikko",
            "4" : "Torstai",
            "5" : "Perjantai",
            "6" : "Lauantai"
        }
        clock.config(text=time.strftime('%H:%M'))
        date.config(text=weekday[time.strftime('%w')]+", "+time.strftime('%d.%m.%Y'))
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)

    tick()

    mainloop()


main()