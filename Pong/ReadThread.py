import serial
from threading import Thread

class MyThread(Thread):
    def __init__(self, val):
        Thread.__init__(self)
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.buffer = '0'
        self.sensor1 = 0
        self.sensor2 = 0
        self.running  = True
        self.isRead1 = True
        self.isRead2 = True
    
    #Infinite loop to read values from sensors
    def run(self):
        while(self.running):
            sensors = self.ser.read()
            if (sensors == "a"):   #Read second captor value
                self.sensor2 = int(self.buffer)
                self.buffer = '0'
                self.isRead2 = False
            elif (sensors == "b"): #Read first captor value
                self.sensor1 = int(self.buffer)
                self.buffer = '0'
                self.isRead1 = False
            else:                  #Otherwise, fill the buffer
                self.buffer += sensors
        
    #Returns the current value of both sensors
    def getSensors(self, id):
        if id == 1:
            self.isRead1 = True
            return self.sensor1
        if id == 2 :
            self.isRead2 = True
            return self.sensor2
        return
    #Stop the thread
    def stop(self):
        self.running = False