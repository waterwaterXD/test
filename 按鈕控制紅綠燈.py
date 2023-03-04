# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
import time
import threading
flag=0
def b1():
    global flag
    flag=~flag
    print(flag)
    if flag==-1:
        button1=Button(root,text="Stop",fg="black",bg="brown",command=b1)
    else:
        button1=Button(root,text="GoGo",fg="black",bg="brown",command=b1)
    button1.pack()
    button1.place(x=h/2-15,y=4)
    
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

def job():
    while True:
        if flag==-1:
            drawlight(1)
            time.sleep(3)
            drawlight(2)
            time.sleep(1.5)
            drawlight(3)
            time.sleep(5)
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

button1=Button(root,text="GoGo",fg="black",bg="brown",command=b1)
button1.pack()
button1.place(x=h/2-15,y=4)

flag =0

t=threading.Thread(target=job)
t.start()

root.mainloop()