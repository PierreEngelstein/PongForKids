import sys,serial
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, val):
        Thread.__init__(self)
        dev='/dev/ttyACM0'
        if sys.platform == 'darwin':   dev='/dev/cu.usbmodem1411'
        if sys.platform == 'win32': dev='COM3'
        self.ser = serial.Serial(dev, 9600)
        self.buffer = "0"
        self.sensor1 = 0
        self.sensor2 = 0
        self.running = True
        self.isRead1 = True
        self.isRead2 = True
    
    #Infinite loop to read values from sensors
    def run(self):
        while(self.running):
            sensors = repr(self.ser.read())
            print(sensors+'\n')
            if (sensors == "b'a'"):   #Read second captor value
                self.sensor2 = int(self.buffer)
                self.buffer = "0"
                self.isRead2 = False
            elif (sensors == "b'b'"): #Read first captor value
                self.sensor1 = int(self.buffer)
                self.buffer = "0"
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