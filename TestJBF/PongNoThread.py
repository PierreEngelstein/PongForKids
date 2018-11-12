from tkinter import *
import SerialReader
import Paddle
import Ball
import math
import random

class PongGame():
    def __init__(self):
        #Start the reader thread
        #self.readerThread = ReadThread.MyThread(10)
        self.readerThread=SerialReader.SerialReader()

        #Frame parameters
        self.width = 1200;
        self.height = 600;
        self.borderWidth = 10;
        
        #Paddle parameters
        self.paddlesDistance = self.width / 120;
        self.paddleThickness = self.width / 40;
        self.paddleLength = 5 * self.height / 24;
        self.paddleMinPos = self.borderWidth + self.paddleLength / 2
        self.paddleMaxPos = self.height - self.borderWidth - self.paddleLength / 2
        
        #Ball parameters
        self.ballRadius = self.width / 100
        self.ballPosX = self.width / 2
        self.ballPosY = self.height / 2
        self.ballSpeed = 10
        
        #Start the tkinter context
        self.root = Tk()
        self.root.title("Pong")
        self.canvas = Canvas(self.root, width = self.width, height = self.height, bg='#101010')
        self.debugText = self.canvas.create_text(50, 50, text="", fill="#EEEEEE") #Debug text, to print current values of the sensors
        self.canvas.focus_set()
        self.root.protocol("WM_DELETE_WINDOW", self.close) #Set a custom close function to be able to stop the reader thread on closing the frame
        
        #The 2 paddles
        self.paddleLeft = Paddle.Paddle(self.canvas, self.paddlesDistance, self.paddleThickness, self.paddleLength, self.height / 2, self.paddleMinPos, self.paddleMaxPos)
        self.paddleRight = Paddle.Paddle(self.canvas, self.width - self.paddlesDistance - self.paddleThickness, self.paddleThickness, self.paddleLength, self.height / 2, self.paddleMinPos, self.paddleMaxPos)
        
        #The ball
        self.ball = Ball.Ball(self.canvas, self.ballPosX, self.ballPosY, self.ballRadius, -math.pi/3, self.ballSpeed)
        
        #The values of the sensors
        self.sensor1 = 0
        self.sensor2 = 0
    
        self.update()
        self.root.mainloop()

    #Update the game
    def update(self):
        #Update the debug text to the current sensor values
        self.sensor1,self.sensor2=self.readerThread.getValues()
        self.canvas.itemconfigure(self.debugText,
                                  text="Sensor 1 : " + str(self.sensor1) + "\nSensor 2 : " + str(self.sensor2))
        self.paddleLeft.update(self.sensor1)
        self.paddleRight.update(self.sensor2)
        self.ball.update(self.width, self.height, self.paddleLeft, self.paddleRight)
        self.canvas.pack()
        self.root.after(10, self.update)

    #Custom close method : stop the reader thread and stop the TKinter frame
    def close(self):
        self.readerThread.ser.close()
        self.root.destroy()

###########################
game = PongGame() #Start the pong game

# def pascal(n):
#     line = [1]
#     for k in range(n):
#         line.append(line[k] * (n-k) / (k+1))
#     return line
# print pascal(8)

