#!/usr/bin/python

from tkinter import *
import requests
import os.path
from PIL import Image, ImageTk
import time

import trello_connect
import yle_connect
import wu_connect

APPNAME = "JAMES"
MF_WIDTH = 800
MF_HEIGHT = 600

FONTFACE = "Helvetica Neue Thin"
FONTWEIGHT = "normal"
TINYFONT = 6
SMALLFONT = 14
MEDIUMFONT = 20
LARGEFONT = 60
WEEKDAY = {
    "0": "Sunnuntai",
    "1": "Maanantai",
    "2": "Tiistai",
    "3": "Keskiviikko",
    "4": "Torstai",
    "5": "Perjantai",
    "6": "Lauantai"
}


def tick():
    clock.config(text=time.strftime('%H:%M'))
    date.config(text=WEEKDAY[time.strftime('%w')]+", "+time.strftime('%d.%m.%Y'))
    clock.after(200, tick)  # Update every 0.2 seconds
    
    
def newsflash():
    newsdata = yle_connect.get_headlines()
    for i in range(len(newsdata)):
        Label(news_f, text=newsdata[i],
              font=(FONTFACE, SMALLFONT, FONTWEIGHT), fg="white", bg="black") \
            .grid(row=i, column=0, sticky=W)
    Label(news_f, text="Päivitetty %s" % time.strftime("%d.%m. %H:%M", time.localtime()),
          font=(FONTFACE, TINYFONT, "italic"), fg="white", bg="black") \
        .grid(row=i + 4, column=0, sticky=W)
    news_f.after(60000, newsflash)  # Update every minute


def weather_update():
    weatherdata = wu_connect.get_weather()
    for r1 in range(0, len(weatherdata[0])):
        fontsize = MEDIUMFONT
        if r1 == 0:
            fontsize = LARGEFONT
        Label(weather_f, text=weatherdata[0][r1],
              font=(FONTFACE, fontsize, FONTWEIGHT), fg="white", bg="black") \
            .grid(row=r1, column=0, sticky=W, columnspan=4)

    v_separator20 = Frame(weather_f, height=20, bg="black")
    v_separator20.grid(row=3, column=0)

    for c in range(1, len(weatherdata)):
        for r in range(0, len(weatherdata[c])):
            Label(weather_f, text=weatherdata[c][r],
                  font=(FONTFACE, SMALLFONT, FONTWEIGHT), fg="white", bg="black") \
                .grid(row=c + 3, column=r, sticky=W)
    Label(weather_f, text="Päivitetty %s" % time.strftime("%d.%m. %H:%M", time.localtime()),
          font=(FONTFACE, TINYFONT, "italic"), fg="white", bg="black") \
        .grid(row=c + 4, column=0, sticky=W)

    weather_f.after(300000, weather_update)  # Update every five minutes


def todos():
    tododata = trello_connect.get_items()
    for i in range(len(tododata)):
        Label(todo_f, text=tododata[i][0],
              font=(FONTFACE, SMALLFONT, FONTWEIGHT), fg="white", bg="black") \
            .grid(row=i, column=0, sticky=W)
    news_f.after(5000, todos)


# ------------------ APP STARTS HERE ------------------


win = Tk(baseName=APPNAME)
win.wm_title(APPNAME)
win.config(bg="black")

mf = Frame(win)
mf.pack_propagate(False)
mf.config(bg="black")
mf.grid(row=0, column=0)

weather_f = Frame(mf)
weather_f.grid(row=0, column=0, sticky="NW")
weather_f.config(bg="black")

v_separator50 = Frame(mf, height=50)
v_separator50.grid(row=2, column=0)
v_separator50.config(bg="black")

news_f = Frame(mf)
news_f.grid(row=3, column=0, sticky="NW")
news_f.config(bg="black")

h_separator100 = Frame(mf, width=100)
h_separator100.grid(row=0, column=1)
h_separator100.config(bg="black")

clock_f = Frame(mf)
clock_f.grid(row=0, column=2, sticky=NW)
clock_f.config(bg="black")
clock = Label(clock_f, font=(FONTFACE, LARGEFONT, FONTWEIGHT), fg="white", bg="black")
clock.grid(row=0, column=1, sticky=E)
date = Label(clock_f, font=(FONTFACE, MEDIUMFONT, FONTWEIGHT), fg="white", bg="black")
date.grid(row=1, column=0, sticky=E, columnspan=2)

todo_f = Frame(mf)
todo_f.grid(row=3, column=2, sticky="NW")
todo_f.config(bg="black")

weather_update()

newsflash()

tick()

todos()

mainloop()
