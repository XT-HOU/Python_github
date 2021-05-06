# ！/usr/bin/python3
# -*- coding:utf-8 -*-

from tkinter import *

class Application(Frame):
    def __init__(self,master =None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLable = Label(self,text='Hello,world!')
        self.helloLable.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

app= Application()
app.master.title("HOU")
print(type(app))
app.mainloop()