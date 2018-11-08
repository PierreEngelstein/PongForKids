import serial
from threading import Thread

class MyThread(Thread):
    def __init__(self, val):
        Thread.__init__(self)
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.prec = 0
        self.buff = '0'
        self.valA = 0
        self.valB = 0
    def run(self):
        while(True):
            values = self.ser.read()
            if (values == "a"):     #Read second captor value
                self.valB = int(self.buff)
                self.buff = '0'
#                 print "B : " + str(self.valB)
            elif (values == "b"):     #Read first captor value
                self.valA = int(self.buff)
                self.buff = '0'
#                 print "A : " + str(self.valA)
            else:
                self.buff += values
    
    def getValues(self):
        return self.valA, self.valB