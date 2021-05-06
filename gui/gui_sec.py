# ！/usr/bin/python3
# -*- coding:utf-8 -*-
from tkinter import *

def createWidgets(self):
    self.helloLable = Label(self, text='Hello,world!')
    self.helloLable.pack()
    self.quitButton = Button(self, text='Quit', command=self.quit)
    self.quitButton.pack()
    self.quitButton.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

top = Tk()
# 这里四个参数分别为：宽、高、左、上
top.geometry("500x300+750+200")
top.title("www.tianqiweiqi.com")
createWidgets(top)
top.mainloop();