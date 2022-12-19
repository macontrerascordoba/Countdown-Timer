import os
import time

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