import keyboard
import Time_counter_revisited_functions as func
import threading
        

clock = func.CounterThread()
clock.setRun()

#Mode type input
while True:
    try:
        Mode = int(input("Type mode number: 1 for Timer (Increase), 2 for Counter (decrease): "))
        break
    except ValueError as e:
        print("Error!")
        Mode = int(input("Type mode number: 1 for Timer (Increase), 2 for Counter (decrease): "))

if Mode == 2: #Mode is counter, more data need to get initiallized.
    clock.clockType = False #Decreasing count
    
    #Input of starting Time
    while True:
        try:
            startingTime = str(input("Input your starting time in this format  hh:mm:ss :"))
            if not func.validate_time_format(startingTime):
                raise ValueError()
            break
        except ValueError as e:
            print("Wrong data/format type.")
    
    clock.setTime(unparsedString = startingTime)

clock.start()

while True:
        if clock.clockType:
            keyboard.wait('w')
            clock.stop()
            print("Stopping Timer...")
            break
        else:
            if clock.getRun():
                break

