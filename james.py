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


def destroy_widgets_in(frame):
    for child in frame.winfo_children():
        child.grid_forget()
        child.destroy()
        del child


def add_frame(parent, height, width, row, column, sticky="NW", bg="black"):
    frame = Frame(parent, height=height, width=width, bg=bg)
    frame.grid(row=row, column=column, sticky=sticky)
    return frame


def tick():
    clock.config(text=time.strftime('%H:%M'))
    date.config(text=WEEKDAY[time.strftime('%w')]+", "+time.strftime('%d.%m.%Y'))
    clock.after(200, tick)  # Update every 0.2 seconds
    
    
def newsflash():
    destroy_widgets_in(news_f)
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
    destroy_widgets_in(weather_f)
    weatherdata = wu_connect.get_weather()
    for r1 in range(0, len(weatherdata[0])):
        fontsize = MEDIUMFONT
        if r1 == 0:
            fontsize = LARGEFONT
        Label(weather_f, text=weatherdata[0][r1],
              font=(FONTFACE, fontsize, FONTWEIGHT), fg="white", bg="black") \
            .grid(row=r1, column=0, sticky=W, columnspan=4)

        add_frame(weather_f, 20, None, 3, 0)

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

mf = add_frame(win, None, None, 0, 0)
mf.pack_propagate(False)

weather_f = add_frame(mf, None, None, 0, 0)

add_frame(mf, 50, 10, 2, 0)  # Separator

news_f = add_frame(mf, None, None, 3, 0)

add_frame(mf, 10, 100, 0, 1)  # Separator

clock_f = add_frame(mf, None, None, 0, 2)
clock = Label(clock_f, font=(FONTFACE, LARGEFONT, FONTWEIGHT), fg="white", bg="black")
clock.grid(row=0, column=1, sticky=E)
date = Label(clock_f, font=(FONTFACE, MEDIUMFONT, FONTWEIGHT), fg="white", bg="black")
date.grid(row=1, column=0, sticky=E, columnspan=2)

todo_f = add_frame(mf, None, None, 3, 2)

weather_update()
newsflash()
tick()
todos()

mainloop()
