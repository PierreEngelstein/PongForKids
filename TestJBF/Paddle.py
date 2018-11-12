class Paddle(object):

    def __init__(self, canvas, distance, thickness, length, startPosY, minPos, maxPos):
        self.posX = distance + thickness / 2
        self.posY = startPosY
        self.minPos = minPos
        self.maxPos = maxPos
        self.thickness = thickness
        self.length = length
        self.canvas = canvas
        self.lastPos = []
        self.precision = 10
        self.sensorMin = 50
        self.sensorMax = 400
        self.paddle = self.canvas.create_rectangle(self.posX - thickness/2, self.posY - length / 2, self.posX + thickness / 2, self.posY  + length / 2, fill = "#FFFFFF")
    def update(self, y):
        #smooth the value of y based on the precedent values:
        #valueY = self.smooth(y)
        valueY = y
        valueY = (valueY - self.sensorMin) * (self.maxPos - self.minPos)/ (self.sensorMax - self.sensorMin) + self.minPos
        self.canvas.move(self.paddle, 0, valueY - self.posY)
        self.posY = valueY
        return
    
    def smooth(self, pos):
        self.storePos(pos)
        if (len(self.lastPos) == self.precision):
            triangle = self.pascal(self.precision*2)
            med = 0
            tri = 0;
            for i in range(0, self.precision):
                med += triangle[i] * self.lastPos[i]
                tri += triangle[i]
            med /= tri
            return med
        else:
            return pos

    
    def storePos(self, pos):
        if (len(self.lastPos) == self.precision):
            self.lastPos.remove(self.lastPos[0])
        if(pos < self.sensorMin):
            pos = self.sensorMin
        if(pos > self.sensorMax):
            pos = self.sensorMax
        
        self.lastPos.append(pos)
        return
    
    #Compute pascal's Triangle for smoothing values
    def pascal(self, n):
        line = [1]
        for k in range(n):
            line.append(line[k] * (n-k) / (k+1))
        return line