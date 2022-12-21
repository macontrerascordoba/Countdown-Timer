import json
from tkinter import *
from tkinter import ttk

import TimerSelectorPage as tsp, TimerPage as tp


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Countdown Timer")
        self.geometry("280x300")
        self.hours = self.minutes = self.seconds = 0
        self.finished = False

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (tp.TimerPage, tsp.TimerSelectorPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.finished = True
        self.showFrame("TimerSelectorPage")


    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()
        jsonData = {
            "hours" : self.hours,
            "minutes" : self.minutes,
            "seconds" : self.seconds
        }
        jsonString = json.dumps(jsonData)
        with open('public/time.json', 'w') as f:
            f.write(jsonString)