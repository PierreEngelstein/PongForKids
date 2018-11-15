from tkinter import *
import SerialReaderThread
import Paddle
import Ball
import math, time
import random

class PongGame():
    def __init__(self):
        #Start the reader thread
        #self.readerThread = ReadThread.MyThread(10)
        self.readerThread=SerialReaderThread.SerialReaderThread()
        self.readerThread.setName("Reader")
        self.readerThread.start()
        
        #Frame parameters
        self.width = 1200;
        self.height = 600;
        self.borderWidth = 10;
        
        #Paddle parameters
        self.paddlesDistance = self.width / 120;
        self.paddleThickness = self.width / 80;
        self.paddleLength = self.height / 3;
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
        self.score1 = self.canvas.create_text(self.width/4, self.height/6, text="", fill="#AAAAAA") #Debug text, to print current values of the sensors
        self.score2 = self.canvas.create_text(3*self.width/4, self.height/6, text="", fill="#AAAAAA")
        self.timeText = self.canvas.create_text(self.width/2, self.height/13, text="", fill="#888888")
        self.canvas.focus_set()
        self.root.protocol("WM_DELETE_WINDOW", self.close) #Set a custom close function to be able to stop the reader thread on closing the frame
        
        #The 2 paddles
        self.paddleLeft = Paddle.Paddle(self.canvas, self.paddlesDistance, self.paddleThickness, self.paddleLength, self.height / 2, self.paddleMinPos, self.paddleMaxPos)
        self.paddleRight = Paddle.Paddle(self.canvas, self.width - self.paddlesDistance - self.paddleThickness, self.paddleThickness, self.paddleLength, self.height / 2, self.paddleMinPos, self.paddleMaxPos)
        
        #The ball
        self.ball = Ball.Ball(self.canvas, self.ballPosX, self.ballPosY, self.ballRadius, math.pi/3, self.ballSpeed)
        
        #The values of the sensors
        self.sensor1 = 0
        self.sensor2 = 0

        #The start time
        self.startTime = time.time()
        self.endTime = self.startTime
        #The maximum time of a game
        self.maxTime = 120.0
        self.update()
        self.root.mainloop()

    #Update the game
    def update(self):
        print(random.randint(0,3))
        #Update the debug text to the current sensor values
        self.sensor1,self.sensor2=self.readerThread.getValues()
        #self.canvas.itemconfigure(self.score, font=("Purisa", 15), text="Joueur 1 : " + str(self.ball.player1) + "\t\tJoueur 2 : " + str(self.ball.player2) + "\t\tTemps : %.2f"  % (self.endTime - self.startTime))
        self.canvas.itemconfigure(self.score1, font=("Purisa", 30), text=self.ball.player1)
        self.canvas.itemconfigure(self.score2, font=("Purisa", 30), text=self.ball.player2)
        self.canvas.itemconfigure(self.timeText, font=("Purisa", 15), text="%.2f" % (self.endTime - self.startTime))
        self.paddleLeft.update(self.sensor1)
        self.paddleRight.update(self.sensor2)
        self.ball.update(self.width, self.height, self.paddleLeft, self.paddleRight)
        self.endTime = time.time()
        if(self.endTime - self.startTime > self.maxTime):
            self.canvas.delete("all")
            if(self.ball.player1 > self.ball.player2):
                self.canvas.create_text(self.width/2, self.height/2, font=("Purisa", 30), text = "Le joueur 1 gagne !",  fill="#EEEEEE")
            elif(self.ball.player2 > self.ball.player1):
                self.canvas.create_text(self.width/2, self.height/2, font=("Purisa", 30), text="Le joueur 2 gagne !",  fill="#EEEEEE")
            else:
                self.canvas.create_text(self.width/2, self.height/2, font=("Purisa", 30), text="Egalite !",  fill="#EEEEEE")
            self.canvas.bind("<p>", self.endGame)
        self.canvas.pack()
        self.root.after(10, self.update)
    def endGame(self, event):
        self.readerThread.do_stop = True
        self.readerThread.join()
        self.root.destroy()
    #Custom close method : stop the reader thread and stop the TKinter frame
    def close(self):
        self.readerThread.do_stop=True
        self.readerThread.join()
        self.root.destroy()

###########################
game = PongGame() #Start the pong game

# def pascal(n):
#     line = [1]
#     for k in range(n):
#         line.append(line[k] * (n-k) / (k+1))
#     return line
# print pascal(8)

