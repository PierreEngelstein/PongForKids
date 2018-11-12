import sys,serial
from threading import Thread

class MyThread(Thread):
    def __init__(self, val):
        Thread.__init__(self)
        dev='/dev/ttyACM0'
        if sys.platform == 'darwin':   dev='/dev/cu.usbmodem1411'
        self.ser = serial.Serial(dev, 9600)
        self.prec = 0
        self.buff = '0'
        self.valA = 0
        self.valB = 0
    def run(self):
        while(True):
            values = self.ser.read()
            print(values)
            if (values == "a"):     #Read second captor value
                self.valB = int(self.buff)
                self.buff = '0'
#                 print "B : " + str(self.valB)
            elif (values == "b"):     #Read first captor value
                self.valA = int(self.buff)
                self.buff = '0'
#                 print "A : " + str(self.valA)
            else:
                self.buff += repr(values)
    
    def getValues(self):
        return self.valA, self.valB