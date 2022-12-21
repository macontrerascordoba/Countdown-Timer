import time

import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.colors = {
            'bg' : '#201a1a',
            'sbt' : '#ffb1c8',
            'sbttxt' : '#581a31',
            'qbt' : '#673d0d',
            'qbttxt' : '#ffdcbe',
            'num' : '#ece0e0',
            'title' : '#dbd2d2'
        }

        self.title('Countdown Timer')
        self.geometry('400x300')
        self.resizable(False, False)
        self.configure(bg=self.colors['bg'])



        # TITLE LABEL
        self.titleLabel = tk.Label(self, text='Set the Timer', font=('Consolas bold', 22), fg=self.colors['title'], bg=self.colors['bg'])
        self.titleLabel.place(x=95, y=40)



        x = 140
        yMid = 120

        # NUMBERS
        # HOURS
        self.hours = tk.StringVar()
        self.hoursEntry = tk.Entry(self, textvariable=self.hours, width=2, relief='flat', font=('OCR A Extended', 14), 
                justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg'])
        self.hoursEntry.place(x=x, y=yMid)
        self.hours.set('00')
        
        # MINUTES
        self.minutes = tk.StringVar()
        self.minutesEntry = tk.Entry(self, textvariable=self.minutes, width=2, relief='flat', font=('OCR A Extended', 14), 
                justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg'])
        self.minutesEntry.place(x=x+40, y=yMid)
        self.minutes.set('00')

        #SECONDS
        self.seconds = tk.StringVar()
        self.secondsEntry = tk.Entry(self, textvariable=self.seconds, width=2, relief='flat', font=('OCR A Extended', 14), 
                justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg'])
        self.secondsEntry.place(x=x+80, y=yMid)
        self.seconds.set('00')


        # : LABELS
        tempX = x+24
        self.separator1 = tk.Label(self, text=':', width=1, relief='flat', font=('OCR A Extended', 14), 
                justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg'])
        self.separator1.place(x=tempX, y=yMid)

        self.separator2 = tk.Label(self, text=':', width=1, relief='flat', font=('OCR A Extended', 14), 
                justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg'])
        self.separator2.place(x=tempX+40, y=yMid)


        # ARROWS
        xArrow = x+7
        yTop = 101


        arr1 = tk.Button(self, text='▲', font=('Consolas bold', 8), fg=self.colors['sbttxt'], 
                bg=self.colors['sbt'], border=0, command=lambda : self.updateValues('h', True))
        arr1.place(x=xArrow, y=yTop)

        arr2 = tk.Button(self, text='▼', font=('Consolas bold', 8), fg=self.colors['sbttxt'], 
                bg=self.colors['sbt'], border=0, command=lambda : self.updateValues('h', False))
        arr2.place(x=xArrow, y=yTop+45)
                
                
        arr3 = tk.Button(self, text='▲', font=('Consolas bold', 8), fg=self.colors['sbttxt'], 
                bg=self.colors['sbt'], border=0, command=lambda : self.updateValues('m', True))
        arr3.place(x=xArrow+40, y=yTop)

        arr4 = tk.Button(self, text='▼', font=('Consolas bold', 8), fg=self.colors['sbttxt'], 
                bg=self.colors['sbt'], border=0, command=lambda : self.updateValues('m', False))
        arr4.place(x=xArrow+40, y=yTop+45)


        arr5 = tk.Button(self, text='▲', font=('Consolas bold', 8), fg=self.colors['sbttxt'], 
                bg=self.colors['sbt'], border=0, command=lambda : self.updateValues('s', True))
        arr5.place(x=xArrow+80, y=yTop)

        arr6 = tk.Button(self, text='▼', font=('Consolas bold', 8), fg=self.colors['sbttxt'], 
                bg=self.colors['sbt'], border=0, command=lambda : self.updateValues('s', False))
        arr6.place(x=xArrow+80, y=yTop+45)
        



        # START BUTTON
        self.startButton = tk.Button(self, text='START TIMER', font=('Consolas bold', 15), fg=self.colors['sbttxt'], bg=self.colors['sbt'],
                 border=0, command=lambda: self.startTimer())
        self.startButton.place(x=125, y=195)



        # QUIT BUTTON
        tk.Button(self, text='QUIT', font=('Consolas bold', 15), fg=self.colors['qbttxt'], bg=self.colors['qbt'],
                 border=0, command=self.destroy).place(x=163, y=240)
        

        self.toDestroy = [arr1, arr2, arr3, arr4, arr5, arr6, 
                            self.startButton, self.titleLabel, self.hoursEntry, self.minutesEntry, self.secondsEntry,
                            self.separator1, self.separator2
                         ]
    


    def startTimer(self):
        for widget in self.toDestroy:
            widget.destroy()
        
        x=90
        y=110
        numbers = [self.hours, self.minutes, self.seconds]
        for i in range(3):
            tk.Label(self, textvariable=numbers[i], width=2, relief='flat', font=('OCR A Extended', 30, 'bold'), 
                justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg']).place(x=x+i*73, y=y)
            
            if i < 2:
                tk.Label(self, text=':', width=1, relief='flat', font=('OCR A Extended', 30, 'bold'), 
                    justify = tk.CENTER, fg=self.colors['num'], bg=self.colors['bg']).place(x=x+50+i*73, y=y)
        

        seconds = int(self.hours.get())*3600 + int(self.minutes.get())*60 + int(self.seconds.get())

        while (seconds >= 0):
            try:
                self.winfo_x()
            except:
                quit()

            minute, second = (seconds // 60 , seconds % 60)
            hour = 0

            if minute > 59:
                hour, minute = (minute // 60 , minute % 60)

            
            if hour >= 0 and hour < 10:
                hour = '0'+str(hour)

            if minute >= 0 and minute < 10:
                minute = '0'+str(minute)

            if second >= 0 and second < 10:
                second = '0'+str(second)

            self.hours.set(hour)
            self.minutes.set(minute)
            self.seconds.set(second)

            self.update()
            time.sleep(1)

            if seconds == 0:
                self.hours.set('00')
                self.minutes.set('00')
                self.seconds.set('00')
            
            seconds -= 1

        tk.Label(self, text="TIME'S UP!!!", font=('Consolas bold', 30), fg=self.colors['title'], bg=self.colors['bg']).place(x=75, y=110)



    def updateValues(self, value, sum):

        if value == 'h':
            if sum:
                hour = int(self.hours.get())+1
            else:
                hour = int(self.hours.get())-1


            if hour < 0:
                hour = 0
            elif hour > 99:
                hour = 99

            if hour >= 0 and hour < 10:
                hour = '0'+str(hour)

            self.hours.set(hour)
        
        elif value == 'm':
            if sum:
                minute = int(self.minutes.get())+1
            else:
                minute = int(self.minutes.get())-1

            if minute < 0:
                minute = 0
            elif minute > 59:
                minute = 59

            if minute >= 0 and minute < 10:
                minute = '0'+str(minute)

            self.minutes.set(minute)
        
        else:
            if sum:
                second = int(self.seconds.get())+1
            else:
                second = int(self.seconds.get())-1

            if second < 0:
                second = 0
            elif second > 59:
                second = 59

            if second >= 0 and second < 10:
                second = '0'+str(second)

            self.seconds.set(second)

