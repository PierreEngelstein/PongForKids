import time
import DummyThread
import SerialReaderThread

######################
# Use case 1
######################
'''
myThread = DummyThread.DummyThread()
myThread.start()
for i in range(0,5):
    time.sleep(1)
    print(i,myThread.getValues())
#Without next lines: main does not finish
myThread.do_stop=True #to stop internal loop
myThread.join() #to wait the thread destroys
'''
######################
# Use case 2
######################
'''
import SerialReaderThread
myThread = SerialReaderThread.SerialReaderThread()
myThread.start()
for i in range(0,5):
    time.sleep(1)
    print(i,myThread.getValues())

myThread.do_stop=True #to stop internal loop
myThread.join() #to wait the thread destroys
'''
######################
# Use case 3 : filtering
######################
'''
import SerialReaderThread
from collections import deque
import statistics as st
myThread = SerialReaderThread.SerialReaderThread()
myThread.start()
a_vals=deque([])
#quit()
try:
    while(True):
        time.sleep(1)
        a,b=myThread.getValues()
        a_vals.append(a)
        if len(a_vals) >= 3 : a_vals.popleft()
        af=st.median(a_vals)
        print("Raw:",a, " Filtered:",af)
        print("Raw:",b)
except:
    print("quit")
    myThread.do_stop=True #to stop internal loop
    myThread.join() #to wait the thread destroys
'''

######################
# Use case 4
######################

import SerialReaderThread
myThread = SerialReaderThread.SerialReaderThread()
myThread.start()
try:
    while(True):
        time.sleep(0.5)
        print(myThread.getValues())
except:
    print("quit")
    myThread.do_stop=True #to stop internal loop
    myThread.join() #to wait the thread destroys
