import threading
import winsound #pip install pywin32
import re

def validate_time_format(input_str):
    pattern = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
    return re.match(pattern, input_str)



class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._run = True

        self.time = {
            "Hours" : 0,
            "Minutes" : 0, 
            "Seconds" : 0
            }
        
        self.clockType = True #True for Timer (Increase), False for Counter (Decrease).
        self.soundFile = "c.wav"

    def run(self):
        while self._run:
            
            #If running Timer.
            if self.clockType:
                self.time["Seconds"] += 1
                if self.time["Seconds"] >= 60:
                    self.time["Seconds"] = 0
                    self.time["Minutes"] += 1
                    if self.time["Minutes"] >= 60:
                        self.time["Minutes"] = 0
                        self.time["Hours"] = (self.time["Hours"] + 1) % 24
               
            
            #If running Counter.
            else:
                
                if self.timeFinished():  #checking if counter reached 0.
                    self.display() #printing time
                    self.run = False
                    print("Counter Stopped")
                    self.stop() 
                    continue

                self.time["Seconds"] -= 1
                if self.time["Seconds"] == -1:
                    self.time["Seconds"] = 59
                    self.time["Minutes"] -= 1
                    if self.time["Minutes"] == -1:
                        self.time["Minutes"] = 59
                        self.time["Hours"] = (self.time["Hours"] - 1) % 24
            
            self.display() #printing time
            
    
    def timeFinished(self):
        if self.time["Hours"] == 0 and self.time["Minutes"] == 0 and self.time["Seconds"] == 0:
            return True
        return False

    def stop(self):
        self.setRun(False)
    
    def setRun(self,Value = True):
        self._run = Value

    def getRun(self):
        return self._run
    
    def setTime(self, hours = None, minutes = None, seconds = None, unparsedString = None):
        if unparsedString is not None:
            hours, minutes, seconds = map(int, unparsedString.split(":"))
        self.time["Hours"] = hours
        self.time["Minutes"] = minutes
        self.time["Seconds"] = seconds
    
    def display(self):
        formattedString = "{:02d}:{:02d}:{:02d}".format(self.time["Hours"], self.time["Minutes"], self.time["Seconds"])
        print(formattedString)
        winsound.PlaySound(self.soundFile, winsound.SND_FILENAME)
       