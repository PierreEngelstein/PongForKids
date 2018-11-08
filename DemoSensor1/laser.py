class laser(object):

    def __init__(self, canvas, posx, posy):
        self.posx = posx
        self.posy = posy
        self.canvas = canvas
        self.tkelement = None
        self.dl = 30
    def update(self):
        self.posx += self.dl
        self.canvas.delete(self.tkelement)
        self.tkelement = self.canvas.create_oval(self.posx-30, self.posy-2, self.posx + 30, self.posy + 2, fill = "#752010")
    
    def getPosX(self):
        return self.posx
    
    def delete(self):
        self.canvas.delete(self.tkelement)
        self.tkelement = None