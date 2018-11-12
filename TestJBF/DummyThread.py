import sys,serial,time
from threading import Thread

class DummyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value=0
        self.do_stop=False
    def run(self):
        while(not self.do_stop):
            time.sleep(0.1)
            self.value+=1
    def getValues(self):
        return self.value