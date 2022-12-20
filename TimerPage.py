import time, json
from tkinter import *
from tkinter import ttk

class TimerPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        if self.controller.hours < 10: self.hoursSpace = " " 
        else: self.hoursSpace = ""
        if self.controller.minutes < 10: self.minutesSpace = " " 
        else: self.minutesSpace = ""
        if self.controller.seconds < 10: self.secondsSpace = " " 
        else: self.secondsSpace = ""

        # TIMER LABEL
        titleLabel = ttk.Label(self, text="TIMER", font=("Arial", 20))
        titleLabel.place(x=100, y=30)

        # : LABELS
        separatorLabels = []
        distance = 123
        for i in range(2):
            separatorLabels.append(ttk.Label(self, text=":"))
            separatorLabels[i].place(x=distance, y=130)
            distance += 30

        # HOURS
        self.hoursLabel = ttk.Label(self, text=self.hoursSpace + str(self.hours))
        self.hoursLabel.place(x=100+2, y=130)

        #MINUTES
        self.minutesLabel = ttk.Label(self, text=self.minutesSpace + str(self.minutes))
        self.minutesLabel.place(x=130+2, y=130)

        #SECONDS
        self.secondsLabel = ttk.Label(self, text=self.secondsSpace + str(self.seconds))
        self.secondsLabel.place(x=160+2, y=130)

        #CLOSE BUTTON
        startButton = ttk.Button(self, text="CLOSE", command=lambda: self.controller.destroy)
        startButton.place(x=100, y=220)

    
    def startTimer(self, start=False):

        with open('public/time.json') as f:
            data = json.load(f)
            self.hours = data['hours']
            self.minutes = data['minutes']
            self.seconds = data['seconds']

        if start:

            self.controller.showFrame('TimerPage')

            seconds = self.controller.hours*3600 + self.controller.minutes*60 + self.controller.seconds

            self.hoursLabel.config(text=self.hoursSpace + str(self.hours))
            self.minutesLabel.config(text=self.minutesSpace + str(self.minutes))
            self.secondsLabel.config(text=self.secondsSpace + str(self.seconds))

            print('a')

            while (seconds >= 0):

                self.hoursLabel.config(text=self.hoursSpace + str(self.controller.hours))
                self.minutesLabel.config(text=self.minutesSpace + str(self.controller.minutes))
                self.secondsLabel.config(text=self.secondsSpace + str(self.controller.seconds))

                if (self.controller.seconds == 0):
                    if (self.controller.minutes == 0):
                        self.controller.hours -= 1
                        self.controller.minutes = 59
                        self.controller.seconds = 59
                    else:
                        self.controller.minutes -= 1
                        self.controller.seconds = 59
                
                else:
                    self.controller.seconds -= 1

                if self.controller.hours < 10: self.hoursSpace = " " 
                else: self.hoursSpace = ""
                if self.controller.minutes < 10: self.minutesSpace = " " 
                else: self.minutesSpace = ""
                if self.controller.seconds < 10: self.secondsSpace = " " 
                else: self.secondsSpace = ""

                seconds -= 1
                time.sleep(1)