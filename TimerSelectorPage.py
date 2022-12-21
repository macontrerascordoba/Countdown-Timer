import json, time
from tkinter import *
from tkinter import ttk

import TimerPage as tp


class TimerSelectorPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.hoursSpace = " "
        self.minutesSpace = " "
        self.secondsSpace = " "

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
        hoursLabel = ttk.Label(self, text=self.hoursSpace + str(self.controller.hours))
        hoursLabel.place(x=100+2, y=130)
        hoursUp = ttk.Button(self, text="↑", width=2, command=lambda: self.changeValues("h", False, hoursLabel))
        hoursUp.place(x=100, y=100)
        hoursDown = ttk.Button(self, text="↓", width=2, command=lambda: self.changeValues("h", True, hoursLabel))
        hoursDown.place(x=100, y=160)

        #MINUTES
        minutesLabel = ttk.Label(self, text=self.minutesSpace + str(self.controller.minutes))
        minutesLabel.place(x=130+2, y=130)
        minutesUp = ttk.Button(self, text="↑", width=2, command=lambda: self.changeValues("m", False, minutesLabel))
        minutesUp.place(x=130, y=100)
        minutesDown = ttk.Button(self, text="↓", width=2, command=lambda: self.changeValues("m", True, minutesLabel))
        minutesDown.place(x=130, y=160)

        #SECONDS
        secondsLabel = ttk.Label(self, text=self.secondsSpace + str(self.controller.seconds))
        secondsLabel.place(x=160+2, y=130)
        secondsUp = ttk.Button(self, text="↑", width=2, command=lambda: self.changeValues("s", False, secondsLabel))
        secondsUp.place(x=160, y=100)
        secondsDown = ttk.Button(self, text="↓", width=2, command=lambda: self.changeValues("s", True, secondsLabel))
        secondsDown.place(x=160, y=160)

        #START TIMER
        tpObj = tp.TimerPage(parent=parent, controller=controller)
        startButton = ttk.Button(self, text="START TIMER", command=lambda: tpObj.startTimer())
        startButton.place(x=100, y=220)

    def changeValues(self, value, substract, label):
        
        # HOURS
        if value == "h":
            if substract:
                self.controller.hours -= 1
            else:
                self.controller.hours += 1

                
            if self.controller.hours < 0:
                self.controller.hours = 0
            elif self.controller.hours > 99:
                self.controller.hours = 99
            
            if self.controller.hours < 10:
                self.hoursSpace = " "
            else:
                self.hoursSpace = ""

            label.config(text=self.hoursSpace + str(self.controller.hours))
        

        # MINUTES
        elif value == "m":
            if substract:
                self.controller.minutes -= 1
            else:
                self.controller.minutes += 1
                

            if self.controller.minutes < 0:
                self.controller.minutes = 0
            elif self.controller.minutes > 60:
                self.controller.minutes = 60
            
            if self.controller.minutes < 10:
                self.minutesSpace = " "
            else:
                self.minutesSpace = ""


            label.config(text=self.minutesSpace + str(self.controller.minutes))
        

        # SECONDS
        elif value == "s":
            if substract:
                self.controller.seconds -= 1
            else:
                self.controller.seconds += 1
            
            
            if self.controller.seconds < 0:
                self.controller.seconds = 0
            elif self.controller.seconds > 60:
                self.controller.seconds = 60
            
            if self.controller.seconds < 10:
                self.secondsSpace = " "
            else:
                self.secondsSpace = ""


            label.config(text=self.secondsSpace + str(self.controller.seconds))

    
    

    