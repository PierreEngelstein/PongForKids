import serial

class Display(object):
    
    def __init__(self, root, canvas, height):
        self.root = root
        self.height = height
        self.c = canvas
        self.dotPosX = 10
        self.dotPosY = 10
        self.dot = self.c.create_oval(self.dotPosX-10, self.dotPosY-10, self.dotPosX+10, self.dotPosY+10, fill="#aeaeae")
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.lastPos = []
        self.update()
        self.root.mainloop()
        return

    def update(self):
        try:
            a = int(self.ser.readline())
        except:
            a = 0
        print ("a = " + str(a))
        b = self.smooth(a)
        b = (b-50)*(self.height-20)/350
        print ("b = " + str(b))
        self.c.delete(self.dot)
        self.dot = self.c.create_oval(10, b, 30, b + 20, fill="#aeaeae")
        self.c.pack()
        self.root.after(10, self.update)
        return
    
    def smooth(self, pos):
        #Smooth the value depending on the previous values (Pascal triangle method)
        self.storePos(pos)
        print self.lastPos
        if (len(self.lastPos) == 5):
            med = (self.lastPos[0] + 8*self.lastPos[1] + 28*self.lastPos[2] + 56*self.lastPos[3] + 70*self.lastPos[4])/163
            return med
        else:
            return pos
        
    def storePos(self, pos):
        #Store the last 5 values in an array used for smoothing
        if (len(self.lastPos) == 5):
            self.lastPos.remove(self.lastPos[0])
        if(pos < 50):
            pos = 50
        if(pos > 400):
            pos = 400
        self.lastPos.append(pos)
        return