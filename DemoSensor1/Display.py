import serial,sys
import laser
import Monster
from random import randint
 
class Display(object):
    
    def __init__(self, root, canvas, height):
        self.root = root
        self.height = height
        self.c = canvas
        self.dotPosX = 10
        self.dotPosY = 10
        self.maxPos = 400
        self.isLaser = False
        self.monster = None
        self.score = 0
        self.timeSinceLaser = 0
        self.laser = laser.laser(self.c, self.dotPosX, self.dotPosY)
        self.dot = self.c.create_oval(self.dotPosX-10, self.dotPosY-10, self.dotPosX+10, self.dotPosY+10, fill="#aeaeae")
        self.scoreText = self.c.create_text(1100, 50, fill = "black", anchor = "nw", text = "touche : 0")
        dev='/dev/ttyACM0'
        if sys.platform == 'darwin':   dev='/dev/cu.usbmodem1411'
        if sys.platform == 'win32' : dev='COM4'
        self.ser = serial.Serial(dev, 9600)
        self.lastPos = []
        self.update()
        self.root.mainloop()
        return

    def update(self):
        self.root.bind("<Return>", self.launchLaser)
        try:
            #t=self.ser.readline()
            a=self.ser.readline().decode()
            #a =repr(a)
            a=int(a)
            print(a)
        except:
            a = 0
        self.b = self.smooth(a)
        self.b = (self.b-150)*(self.height-20)/(self.maxPos - 150)
        self.c.delete(self.dot)
        self.dot = self.c.create_oval(10, self.b, 30, self.b + 20, fill="#aeaeae")
        if(self.isLaser):
            #Laser update
            self.timeSinceLaser += 10
            if self.laser.posx >= 1000:
                self.laser.delete()
                self.laser = laser.laser(self.c, self.dotPosX, self.b + 10)
                self.timeSinceLaser = 0
            self.laser.update()
            #Monster update
            if self.monster == None:
                self.monster = Monster.Monster(self.c, 800, randint(50, 550))
            if self.laser.posx >= self.monster.posx and (self.laser.posy <= self.monster.posy + 30 and self.laser.posy >= self.monster.posy - 30):
                print("Killed monster")
                self.monster.delete()
                self.monster = None
                self.score += 1
                self.c.itemconfig(self.scoreText, text = "touche : " + str(self.score))
        else:
            if self.monster != None:
                self.monster.delete()
                self.monster = None
        self.c.pack()
        self.root.after(5, self.update)
        return
    
    def smooth(self, pos):
        #Smooth the value depending on the previous values (Pascal triangle method)
        self.storePos(pos)
        if (len(self.lastPos) == 5):
            med = (self.lastPos[0] + 8*self.lastPos[1] + 28*self.lastPos[2] + 56*self.lastPos[3] + 70*self.lastPos[4])/163
            return med
        else:
            return pos
        
    def storePos(self, pos):
        #Store the last 5 values in an array used for smoothing
        if (len(self.lastPos) == 5):
            self.lastPos.remove(self.lastPos[0])
        if(pos < 150):
            pos = 150
        if(pos > self.maxPos):
            pos = self.maxPos
        self.lastPos.append(pos)
        return

    def launchLaser(self, event):
        self.isLaser = not self.isLaser
        self.laser.delete()
        self.laser = laser.laser(self.c, self.dotPosX, self.b)
        self.timeSinceLaser = 0
        print(self.isLaser)
        