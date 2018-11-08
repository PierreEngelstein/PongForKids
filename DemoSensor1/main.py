from Tkinter import *
import Display

root = Tk()
root.title("string")

c = Canvas(root, width = 1200, height = 600, bg='#eeeeee')

dis = Display.Display(root=root, canvas=c, height = 600)
