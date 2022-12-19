import os, time
from tkinter import *
from tkinter import ttk

# Creating App class which will contain
# Label Widgets
class App:
    def __init__(self, master, hours, minutes, seconds) -> None:
        self.master = master
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def mainFuntionality(self):
        
        # TIMER LABEL
        titleLabel = ttk.Label(self.master, text="TIMER", font=("Arial", 20))
        titleLabel.place(x=600, y=50)

        toErase = []

        # HOURS
        toErase.append(ttk.Label(self.master, text="         " + str(self.hours)))
        toErase[0].place(x=300, y=200)
        hoursUp = ttk.Button(self.master, text="↑", command=lambda: self.changeValues("h", False, hoursLabel))
        hoursUp.place(x=300, y=150)
        hoursDown = ttk.Button(self.master, text="↓", command=lambda: self.changeValues("h", True, hoursLabel))
        hoursDown.place(x=300, y=250)

        #MINUTES
        minutesLabel = ttk.Label(self.master, text="         " + str(self.minutes))
        minutesLabel.place(x=600, y=200)
        minutesUp = ttk.Button(self.master, text="↑", command=lambda: self.changeValues("m", False, minutesLabel))
        minutesUp.place(x=600, y=150)
        minutesDown = ttk.Button(self.master, text="↓", command=lambda: self.changeValues("m", True, minutesLabel))
        minutesDown.place(x=600, y=250)

        #SECONDS
        secondsLabel = ttk.Label(self.master, text="         " + str(self.seconds))
        secondsLabel.place(x=900, y=200)
        secondsUp = ttk.Button(self.master, text="↑", command=lambda: self.changeValues("s", False, secondsLabel))
        secondsUp.place(x=900, y=150)
        secondsDown = ttk.Button(self.master, text="↓", command=lambda: self.changeValues("s", True, secondsLabel))
        secondsDown.place(x=900, y=250)

        #START TIMER
        startButton = ttk.Button(self.master, text="START TIMER", command=lambda: self.startTimer(toErase))
        startButton.place(x=600, y=300)

    def changeValues(self, value, substract, label):
        
        # HOURS
        if value == "h":
            if substract:
                self.hours -= 1
            else:
                self.hours += 1

                
            if self.hours < 0:
                self.hours = 0
            label.config(text="         " + str(self.hours))
        

        # MINUTES
        elif value == "m":
            if substract:
                self.minutes -= 1
            else:
                self.minutes += 1
                

            if self.minutes < 0:
                self.minutes = 0
            label.config(text="         " + str(self.minutes))
        

        # SECONDS
        elif value == "s":
            if substract:
                self.seconds -= 1
            else:
                self.seconds += 1
            
            
            if self.seconds < 0:
                self.seconds = 0
            label.config(text="         " + str(self.seconds))

    
    def startTimer(self, toErase):

        seconds = self.hours*3600 + self.minutes*60 + self.seconds
        toErase[0].destroy

        while (seconds >= 0):

            # TIMER LABEL
            titleLabel = ttk.Label(self.master, text="TIMER", font=("Arial", 20))
            titleLabel.place(x=600, y=50)

            timerText = "     " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
            ttk.Label(self.master, text=timerText, font=("Arial", 20))

            if (self.seconds == 0):
                if (self.minutes == 0):
                    self.hours -= 1
                    self.minutes = 59
                    self.seconds = 59
                else:
                    self.minutes -= 1
                    self.seconds = 59
            
            else:
                self.seconds -= 1

            seconds -= 1
            time.sleep(1)


    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

def main(hours, minutes, seconds):
    root = Tk()
    root.title("Countdown Timer")
    root.geometry("1200x400")

    
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.title("Countdown Timer")
    root.geometry("1200x350")

    hours = 0
    minutes = 0
    seconds = 0

    app = App(root, hours, minutes, seconds)
    app.mainFuntionality()

    root.mainloop()
    
exit()

while True:
    try:
        os.system("clear")

        print("COUNTDOWN TIMER")
        hours = int(input("Hours -> "))
        minutes = int(input("Minutes -> "))
        sec = int(input("Seconds -> "))
    except:
        print("Please introduce valid numbers!!")
        time.sleep(2)
    else:
        break


seconds = hours*3600 + minutes*60 + sec

while (seconds >= 0):
    os.system("clear")
    print("COUNTDOWN TIMER")
    print("     " + str(hours) + ":" + str(minutes) + ":" + str(sec))
    if (sec == 0):
        if (minutes == 0):
            hours -= 1
            minutes = 59
            sec = 59
        else:
            minutes -= 1
            sec = 59
    
    else:
        sec -= 1

    seconds -= 1
    time.sleep(1)

print("\n  TIME'S UP!!")

input("\nPress Enter to exit...")
os.system("clear")