#!/usr/bin/python

from Tkinter import *

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
        self.data = Datastructure()
        self.pack()
        self.createWidgets()


class Datastructure():
    def __init__(self):
        self.omw_data = omw_connect.get_weather()
        self.yle_data = yle_connect.get_headlines()
        self.trello_data = trello_connect.get_items()

    def get_weather(self):
        return self.omw_data

    def get_news(self):
        return self.yle_data

    def get_todos(self):
        return self.trello_data


def main():
    root = Tk()
    root.title("James")
    root.configure(background="black", height="600", width="800")
    app = Application(master=root)
    app.mainloop()
    root.destroy()


main()