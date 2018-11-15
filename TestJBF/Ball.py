import math, time, random
class Ball(object):

    def __init__(self, canvas, posX, posY, radius, angle, speed):
        self.canvas = canvas
        self.initX = posX
        self.initY = posY
        self.posX = self.initX
        self.posY = self.initY
        self.radius = radius
        self.initAngle = angle
        self.angle = self.initAngle
        self.player1 = 0
        self.player2 = 0
        self.ball = self.canvas.create_oval(self.posX - self.radius, self.posY - self.radius, self.posX + self.radius, self.posY + self.radius, fill = "#FFFFFF")
        self.speed = speed
        return
    
    def update(self, width, height, paddleLeft, paddleRight):
        dx = self.speed * math.cos(self.angle)
        dy = self.speed * -math.sin(self.angle)
        self.canvas.move(self.ball, dx, dy)
        self.posX += dx
        self.posY += dy
        #If the ball hit the top or bottom border
        if (self.posY - self.radius < 0) or (self.posY + self.radius > height):
            self.angle = -self.angle
        #if the ball hit the right paddle
        if((self.posX + self.radius > paddleRight.posX - paddleRight.thickness / 2) and (self.posY < paddleRight.posY + paddleRight.length / 2) and (self.posY > paddleRight.posY - paddleRight.length / 2)):
            self.angle = self.angle + math.pi/ 2
        #if the ball hit the left paddle   
        if((self.posX - self.radius < paddleLeft.posX + paddleLeft.thickness / 2) and (self.posY < paddleLeft.posY + paddleLeft.length / 2) and (self.posY > paddleLeft.posY - paddleLeft.length / 2)):
            self.angle = self.angle + math.pi/ 2
        #If the ball hit one of the left or right border
        if(self.posX + self.radius > width):
            self.resetBall(1)

        if(self.posX - self.radius < 0):
            self.resetBall(2)

    def resetBall(self, winner):
        self.posX = self.initX
        self.posY = self.initY
        self.angle = (random.randint(0,89) + 90*random.randint(0,1) - 45)*math.pi/180
        if winner == 1 :
            self.player1 += 1
        else :
            self.player2 += 1
        self.canvas.delete(self.ball)
        self.ball = self.canvas.create_oval(self.posX - self.radius, self.posY - self.radius, self.posX + self.radius, self.posY + self.radius, fill="#FFFFFF")
        #time.sleep(3)
        return
        