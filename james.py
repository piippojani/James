#!/usr/bin/python

import tkinter as tk
# import requests
# import os.path
# from PIL import Image, ImageTk
import time

import trello_connect
import yle_connect
import wu_connect
import pyttsx


class MainApplication(tk.Frame):
    def destroy_widgets_in(self, frame):
        for child in frame.winfo_children():
            child.grid_forget()
            child.destroy()
            del child

    def add_frame(self, parent, height, width, row, column, sticky="NW",
                  bg="black"):
        frame = tk.Frame(parent, height=height, width=width, bg=bg)
        frame.grid(row=row, column=column, sticky=sticky)
        return frame
    
    def tick(self):
        self.clock.config(text=time.strftime('%H:%M'))
        self.date.config(text=(self.config["WEEKDAY"][time.strftime('%w')] +
                               ", " + time.strftime('%d.%m.%Y')))
        self.clock.after(200, self.tick)  # Update every 0.2 seconds
        
    def newsflash(self):
        self.destroy_widgets_in(self.news_f)
        newsdata = yle_connect.get_headlines()
        for i in range(len(newsdata)):
            tk.Label(self.news_f, text=newsdata[i],
                     font=(self.config["FONT_FACE"],
                           self.config["SMALL_FONT"],
                           self.config["FONT_WEIGHT"]),
                     fg="white", bg="black") \
                .grid(row=i, column=0, sticky="W")
        tk.Label(self.news_f,
                 text="Päivitetty %s" %
                      time.strftime("%d.%m. %H:%M", time.localtime()),
                 font=(self.config["FONT_FACE"], self.config["TINY_FONT"],
                       "italic"), fg="white", bg="black") \
            .grid(row=i + 4, column=0, sticky="W")
        self.news_f.after(60000, self.newsflash)  # Update every minute
    
    def weather_update(self):
        self.destroy_widgets_in(self.weather_f)
        weather_data = wu_connect.get_weather()
        for r1 in range(0, len(weather_data[0])):
            font_size = self.config["MEDIUM_FONT"]
            if r1 == 0:
                font_size = self.config["LARGE_FONT"]
            tk.Label(self.weather_f, text=weather_data[0][r1],
                     font=(self.config["FONT_FACE"], font_size,
                           self.config["FONT_WEIGHT"]),
                     fg="white", bg="black") \
                .grid(row=r1, column=0, sticky="W", columnspan=4)

            self.add_frame(self.weather_f, 20, None, 3, 0)
    
        for c in range(1, len(weather_data)):
            for r in range(0, len(weather_data[c])):
                tk.Label(self.weather_f, text=weather_data[c][r],
                         font=(self.config["FONT_FACE"],
                               self.config["SMALL_FONT"],
                               self.config["FONT_WEIGHT"]),
                         fg="white", bg="black") \
                    .grid(row=c + 3, column=r, sticky="W")
    
        tk.Label(self.weather_f,
                 text="Päivitetty %s" %
                      time.strftime("%d.%m. %H:%M", time.localtime()),
                 font=(self.config["FONT_FACE"], self.config["TINY_FONT"],
                       "italic"), fg="white", bg="black") \
            .grid(row=c + 4, column=0, sticky="W")
        # Update every five minutes
        self.weather_f.after(300000, self.weather_update)
    
    def todos(self):
        todo_data = trello_connect.get_items()
        for i in range(len(todo_data)):
            tk.Label(self.todo_f, text=todo_data[i][0],
                     font=(self.config["FONT_FACE"],
                           self.config["SMALL_FONT"],
                           self.config["FONT_WEIGHT"]),
                     fg="white", bg="black") \
                .grid(row=i, column=0, sticky="W")
        self.news_f.after(5000, self.todos)

    def read_news(self):
        engine = pyttsx.init()
        for item in yle_connect.get_headlines():
            engine.say(item)
        engine.runAndWait()
        engine.stop()


    def __init__(self, master):
        self.config = {
            "APP_NAME": "JAMES",
            "MF_WIDTH": 800,
            "MF_HEIGHT": 600,
            "FONT_FACE": "Helvetica Neue Thin",
            "FONT_WEIGHT": "normal",
            "TINY_FONT": 6,
            "SMALL_FONT": 14,
            "MEDIUM_FONT": 20,
            "LARGE_FONT": 60,
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
        self.master.wm_title(self.config["APP_NAME"])
        self.master.config(bg="black")

        self.mf = self.add_frame(master, None, None, 0, 0)
        self.mf.pack_propagate(False)

        self.weather_f = self.add_frame(self.mf, None, None, 0, 0)

        self.add_frame(self.mf, 50, 10, 2, 0)  # Separator

        self.news_f = self.add_frame(self.mf, None, None, 3, 0)

        self.add_frame(self.mf, 10, 100, 0, 1)  # Separator

        self.clock_f = self.add_frame(self.mf, None, None, 0, 2)
        self.clock = tk.Label(self.clock_f,
                              font=(self.config["FONT_FACE"],
                                    self.config["LARGE_FONT"],
                                    self.config["FONT_WEIGHT"]),
                              fg="white", bg="black")
        self.clock.grid(row=0, column=1, sticky="E")
        self.date = tk.Label(self.clock_f, font=(self.config["FONT_FACE"],
                                                 self.config[
                                                     "MEDIUM_FONT"],
                                                 self.config[
                                                     "FONT_WEIGHT"]),
                             fg="white", bg="black")
        self.date.grid(row=1, column=0, sticky="E", columnspan=2)

        self.todo_f = self.add_frame(self.mf, None, None, 3, 2)

        self.buttons_f = self.add_frame(self.mf, None, None, 4, 2)

        self.read_news_btn = tk.Button(self.buttons_f,
                                       text="Uutiset",
                                       command=self.read_news)
        self.read_news_btn.grid(row=0, column=0)

        self.weather_update()
        self.newsflash()
        self.tick()
        self.todos()


def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()
