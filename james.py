#!/usr/bin/python

import tkinter as tk
import requests
import os.path
from PIL import Image, ImageTk
import time

import trello_connect
import yle_connect
import wu_connect


class MainApplication(tk.Frame):
    def __init__(self, master):
        self.config = {
            "APPNAME": "JAMES",
            "MF_WIDTH": 800,
            "MF_HEIGHT": 600,
            "FONTFACE": "Helvetica Neue Thin",
            "FONTWEIGHT": "normal",
            "TINYFONT": 6,
            "SMALLFONT": 14,
            "MEDIUMFONT": 20,
            "LARGEFONT": 60,
            "WEEKDAY": {
                "0": "Sunnuntai",
                "1": "Maanantai",
                "2": "Tiistai",
                "3": "Keskiviikko",
                "4": "Torstai",
                "5": "Perjantai",
                "6": "Lauantai"
            }
        }
        self.master = master
        self.master.wm_title(self.config["APPNAME"])
        self.master.config(bg="black")
        
        self.mf = self.add_frame(master, None, None, 0, 0)
        self.mf.pack_propagate(False)

        self.weather_f = self.add_frame(self.mf, None, None, 0, 0)

        self.add_frame(self.mf, 50, 10, 2, 0)  # Separator

        self.news_f = self.add_frame(self.mf, None, None, 3, 0)

        self.add_frame(self.mf, 10, 100, 0, 1)  # Separator

        self.clock_f = self.add_frame(self.mf, None, None, 0, 2)
        self.clock = tk.Label(self.clock_f, font=(self.config["FONTFACE"], self.config["LARGEFONT"], self.config["FONTWEIGHT"]), fg="white", bg="black")
        self.clock.grid(row=0, column=1, sticky="E")
        self.date = tk.Label(self.clock_f, font=(self.config["FONTFACE"], self.config["MEDIUMFONT"], self.config["FONTWEIGHT"]), fg="white", bg="black")
        self.date.grid(row=1, column=0, sticky="E", columnspan=2)

        self.todo_f = self.add_frame(self.mf, None, None, 3, 2)

        self.weather_update()
        self.newsflash()
        self.tick()
        self.todos()

    def destroy_widgets_in(self, frame):
        for child in frame.winfo_children():
            child.grid_forget()
            child.destroy()
            del child
    
    def add_frame(self, parent, height, width, row, column, sticky="NW", bg="black"):
        frame = tk.Frame(parent, height=height, width=width, bg=bg)
        frame.grid(row=row, column=column, sticky=sticky)
        return frame
    
    def tick(self):
        self.clock.config(text=time.strftime('%H:%M'))
        self.date.config(text=self.config["WEEKDAY"][time.strftime('%w')]+", "+time.strftime('%d.%m.%Y'))
        self.clock.after(200, self.tick)  # Update every 0.2 seconds
        
    def newsflash(self):
        self.destroy_widgets_in(self.news_f)
        newsdata = yle_connect.get_headlines()
        for i in range(len(newsdata)):
            tk.Label(self.news_f, text=newsdata[i],
                     font=(self.config["FONTFACE"], 
                           self.config["SMALLFONT"], 
                           self.config["FONTWEIGHT"]), 
                     fg="white", bg="black") \
                .grid(row=i, column=0, sticky="W")
        tk.Label(self.news_f, text="Päivitetty %s" % time.strftime("%d.%m. %H:%M", time.localtime()),
                 font=(self.config["FONTFACE"], self.config["TINYFONT"], "italic"), fg="white", bg="black") \
            .grid(row=i + 4, column=0, sticky="W")
        self.news_f.after(60000, self.newsflash)  # Update every minute
    
    def weather_update(self):
        self.destroy_widgets_in(self.weather_f)
        weatherdata = wu_connect.get_weather()
        for r1 in range(0, len(weatherdata[0])):
            fontsize = self.config["MEDIUMFONT"]
            if r1 == 0:
                fontsize = self.config["LARGEFONT"]
            tk.Label(self.weather_f, text=weatherdata[0][r1],
                  font=(self.config["FONTFACE"], fontsize, self.config["FONTWEIGHT"]), fg="white", bg="black") \
                .grid(row=r1, column=0, sticky="W", columnspan=4)

            self.add_frame(self.weather_f, 20, None, 3, 0)
    
        for c in range(1, len(weatherdata)):
            for r in range(0, len(weatherdata[c])):
                tk.Label(self.weather_f, text=weatherdata[c][r],
                      font=(self.config["FONTFACE"], self.config["SMALLFONT"], self.config["FONTWEIGHT"]), fg="white", bg="black") \
                    .grid(row=c + 3, column=r, sticky="W")
    
        tk.Label(self.weather_f, text="Päivitetty %s" % time.strftime("%d.%m. %H:%M", time.localtime()),
              font=(self.config["FONTFACE"], self.config["TINYFONT"], "italic"), fg="white", bg="black") \
            .grid(row=c + 4, column=0, sticky="W")

        self.weather_f.after(300000, self.weather_update)  # Update every five minutes
    
    def todos(self):
        tododata = trello_connect.get_items()
        for i in range(len(tododata)):
            tk.Label(self.todo_f, text=tododata[i][0],
                  font=(self.config["FONTFACE"], self.config["SMALLFONT"], self.config["FONTWEIGHT"]), fg="white", bg="black") \
                .grid(row=i, column=0, sticky="W")
        self.news_f.after(5000, self.todos)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()
