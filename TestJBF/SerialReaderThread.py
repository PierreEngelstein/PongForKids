import sys,serial,time
from threading import Thread
from collections import deque
import statistics as st
import re


class SerialReaderThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.do_stop = False
        dev='/dev/ttyACM0'
        if sys.platform == 'darwin':   dev='/dev/cu.usbmodem1411'
        if sys.platform == 'win32': dev='COM3'
        self.ser = serial.Serial(dev, 9600)
        self.a_vals=deque([])
        self.b_vals=deque([])
        self.valA = 0
        self.valB = 0
        self.filter_size=3
    def run(self):
        while(not self.do_stop):
            #time.sleep(1)
            try:
                #Read 10
                values = repr(self.ser.read(15))
                #self.ser.flushInput()
                #VALUE DETECTION
                raw_a=int(re.findall('a\d+b',values)[-1][1:-1])
                raw_b =int(re.findall('b\d+a',values)[-1][1:-1])
                #FILTERING
                self.a_vals.append(raw_a)
                self.valA=st.mean(self.a_vals)
                if len(self.a_vals) >= self.filter_size : self.a_vals.popleft()
                self.b_vals.append(raw_b)
                self.valB=st.mean(self.b_vals)
                if len(self.b_vals) >= self.filter_size : self.b_vals.popleft()
            except:pass
        #WHEN STOP -> CLOSE CONNEXION
        self.ser.close()
    
    def getValues(self):
        return self.valA, self.valB
