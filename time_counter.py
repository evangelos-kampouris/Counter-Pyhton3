import threading
import win32api
import time
import winsound

filename  =  "c.wav"
keypress = False

def Next_num(list,index,Bool = False):
    if not Bool:
        if list[index] - 1 != -1:
            return True
    else:
        if list[index] + 1 != 61:
            return True
    return False
def countEnded(time):
    if time == 0:
        return True
    return False
def modeInput():
    print("Για χρονόμετρο επιλέξετε το 1, Για αντίστροφη μέτρηση επίλέξτε το 2")
    try:
        inp = int(input())
    except ValueError as e:
        print("Λάθος εισαγωγή" , end = " ")
        print("Για χρονόμετρο επιλέξετε το 1, Για αντίστροφη μέτρηση επίλέξτε το 2")
        inp = int(input())
    if inp == 2:
        return -1
    return 1
def unformatDate(time):
    list = time.split(":")
    int_time = time.replace(":","")
    int_timex = int(int_time)
    for x in list:
        list = [int(x) for x in list]
    return [list,int_time]
def formatDate(list,between = ""):
    date = ""
    for i in range(3):
        if i < 2:
            date += "{:02d}".format(list[i]) + between
        else:
            date += "{:02d}".format(list[i])
    return date
def capture_key():
    global keypress
    while not keypress:
        a = win32api.GetKeyState(0x57)
        if a < 0:
            print("W Pressed")
            keypress = True
        time.sleep(0.1)
#Main
if modeInput() == -1:
    time_inp = input("Δώσε χρόνο:")
    timel,timex = unformatDate(time_inp)
    print(time_inp)
    time.sleep(1)
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    while not countEnded(time_inp):
        if Next_num(timel,2):
            timel[2] -= 1
        else:
            if Next_num(timel,1):
                timel[1] -= 1
                timel[2] = 59
                if Next_num(timel,0):
                    timel[0] -= 1
                    timel[1] = 59
                    timel[2] = 59
        time_inp = int(formatDate(timel))
        time_print = formatDate(timel,":")
        print(time_print)
        winsound.PlaySound(filename, winsound.SND_FILENAME)
else:
    time_inp = "00:00:00"
    print(time_inp)
    time.sleep(1)
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    timel,timex = unformatDate(time_inp)
    p = threading.Thread(target = capture_key)
    p.start()
    while not keypress:
    #while True:
        if  Next_num(timel,2,True):
            timel[2] += 1
        else:
            if Next_num(timel,1,True):
                timel[1] = 0
                timel[2] += 1
                if Next_num(timel,0):
                    timel[0] = 0
                    timel[1] = 0
                    timel[2] += 1
        time_inp = int(formatDate(timel))
        print(formatDate(timel,":"))
        winsound.PlaySound(filename, winsound.SND_FILENAME)