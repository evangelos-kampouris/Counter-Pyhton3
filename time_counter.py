from playsound import playsound

def NextNotNeg(list,index):
    if list[index] - 1 != -1:
        return True
    return False
def countEnded(time):
    if time == 0:
        return True
    return False
def formatDate(list,between = ""):
    date = ""
    for i in range(3):
        if i < 2:
            date += "{:02d}".format(list[i]) + between
        else:
            date += "{:02d}".format(list[i])
    return date

sound = "C:/Users/vaggo/Downloads/Clock.mp3"

x = "00:01:05"
print(x)
playsound(sound)
timel = x.split(":")
timex = x.replace(":","")

for x in timel:
    timel = [int(x) for x in timel]

while not countEnded(int(timex)):
    if NextNotNeg(timel,2):
        timel[2] -= 1
    else:
        if NextNotNeg(timel,1):
           timel[1] -= 1
           timel[2] = 59
        else:
            if NextNotNeg(timel,0):
                timel[0] -= 1
                timel[1] = 59
                timel[2] = 59
    
    timex = formatDate(timel)
    time_print = formatDate(timel,":")
    print(time_print)
    playsound(sound)
    