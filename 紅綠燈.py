# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:54:23 2022

@author: ajlov
"""
from tkinter import *
import time
import threading

def drawlight(num):
    c.create_oval(w/2-r ,h/2-r,w/2+r,h/2+r,fill="black")
    c.create_oval(w/2-r-100 ,h/2-r,w/2+r-100,h/2+r,fill="black")
    c.create_oval(w/2-r+100 ,h/2-r,w/2+r+100,h/2+r,fill="black")
    if (num==1):
        c.create_oval(w/2-r-100 ,h/2-r,w/2+r-100,h/2+r,fill="green")
    if (num==2):
        c.create_oval(w/2-r ,h/2-r,w/2+r,h/2+r,fill="yellow")
    if(num==3):
        c.create_oval(w/2-r+100 ,h/2-r,w/2+r+100,h/2+r,fill="red")

root=Tk()
BF=Frame(root)
BF.pack()
h=400
w=400
r=35
c=Canvas(BF,height=h,width=w,bg="blue")
c.pack()

c.create_rectangle(w/2-150,h/2-60,w/2+150,h/2+60,fill="brown")
c.create_oval(w/2-r,h/2-r,w/2+r,h/2+r,fill="black")
c.create_oval(w/2-r-100,h/2-r,w/2+r-100,h/2+r,fill="black")
c.create_oval(w/2-r+100,h/2-r,w/2+r+100,h/2+r,fill="black")

def job():
    while True:
        drawlight(1)
        time.sleep(3)
        drawlight(2)
        time.sleep(1.5)
        drawlight(3)
        time.sleep(5)

t=threading.Thread(target=job)
t.start()

root.mainloop()
        
