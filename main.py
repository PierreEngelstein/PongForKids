from Tkinter import *
from Display import Display

root = Tk()
root.title("string")

c = Canvas(root, width = 1200, height = 600, bg='#846298')

dis = Display(root=root, canvas=c, height = 600)
