# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:29:58 2022

@author: ajlov
"""
from tkinter import *
from tkinter import ttk
import time

root =Tk()
root.title('Progress Bar')
w=Canvas(root,bg='pink',width=640,height=400)
w.pack()

def run():
    progressBar['maximum']=100
    progressBar['value']=0
    color1=[1,2,3,4,5]
    color1[0]='yellow';color1[1]='blue';color1[2]='brown';
    color1[3]='red';color1[4]='green';
    Label(root,text="     ",bg="green").place(x=320-140,y=350-30)
    r =100
    for i in range(0,101,5):
        progressBar['value']=i
        w.create_oval(320-(r-i),200-(r-i),320+(r-i),200+(r-i),fill=color1[int(i/5)%5])
        time.sleep(0.2)
        Label(root,text=str(i),bg='green').place(x=320-140,y=350-30)
        progressBar.update()
        
button1 = Button(root,bg ='Lime',text='Run Progress Bar',command=run)
button1.place(x=260,y=30)

progressBar=ttk.Progressbar(root,orient='horizontal',length=300,mode='determinate')
progressBar.place(x=320-140,y=350)

root.mainloop()
