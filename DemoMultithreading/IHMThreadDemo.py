from Tkinter import *
import ReadThread

class IHM():
    def __init__(self):
        self.thread1 = ReadThread.MyThread(10)
        self.thread1.setName("Thread 1")
        self.thread1.start()
        self.root = Tk()
        self.root.title("string")
        self.c = Canvas(self.root, width = 1200, height = 600, bg='#846298')
        self.blah = self.c.create_text(50, 50, text="blah")
        self.c.focus_set()
        self.c.bind("<Button-1>", self.click)
        self.update()
        self.root.mainloop()
        
    def update(self):
        self.c.itemconfigure(self.blah, text="A : " + str(self.thread1.getValues()[0]) + "\nB : " + str(self.thread1.getValues()[1]))
        self.c.pack()
        self.root.after(10, self.update)
        
        return
    def click(self, event):
        print "BLAHHHHHHHHHHIHM"
        return