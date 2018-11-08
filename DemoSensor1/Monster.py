import PIL.Image
from Tkinter import *
from random import randint


class Monster(object):

    def __init__(self, canvas, posx, posy):
        self.posx = posx
        self.posy = posy
        self.canvas = canvas
        SkinID = randint(1, 2)
        self.tkelement = None
        image = PIL.Image.open("SpaceInvader_Enemy" + str(SkinID) + ".png")
        image = image.resize((60, 60))
        image.save("imgResized/SpaceInvader_Enemy" + str(SkinID) + ".png", "png")
        self.pic = PhotoImage(file = "imgResized/SpaceInvader_Enemy" + str(SkinID) + ".png")
        self.form = canvas.create_image(self.posx, self.posy, image = self.pic)
        
    def getPosX(self):
        return self.posx
    
    def delete(self):
        self.canvas.delete(self.form)
        self.form = None