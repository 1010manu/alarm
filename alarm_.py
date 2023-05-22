import datetime
from playsound import playsound
Hour = int(input("Enter Hour: "))
Min = int(input("Enter Minutes: "))
ap = input("am / pm: ")
if ap=="pm":
    Hour+=12
while True:

    if Hour==datetime.datetime.now().hour and Min==datetime.datetime.now(). minute:
        print("time to wake up")
        
        break
