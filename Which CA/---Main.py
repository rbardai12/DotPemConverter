import py_compile
from turtle import left, right, width
import requests
from tkinter import *
import sys
import os
import subprocess


#Button Main
root = Tk()
root.title("Choose CA Certificate")
root.geometry('1100x350')


#Commands For Scripts
def CRTcommand():
    os.system('python CRT.py')

def CERcommand():
    os.system('python CER.py')

def p7bcommand():
    os.system('python P7B.py')

def PFXcommand():
    os.system('python PFX.py')

def P12command():
    os.system('python P12.py')

def help():
    os.system('python Help.py')


#Buttons
l = Label(root, text='Select the CA Certificate you have')
l.pack()

a = Button(root, text='CRT', command= CRTcommand,
                width=30,
                height=8)
a.pack(side=RIGHT)

a2 = Button(root, text='CER', command= CERcommand,
                width=30,
                height=8)
a2.pack(side=RIGHT)

b = Button(root, text='PFX', command= PFXcommand,
                width=30,
                height=8)
b.pack(side=LEFT)

b2 = Button(root, text='P12', command= P12command,
                width=30,
                height=8)
b2.pack(side=LEFT)

c = Button(root, text='P7B', command= p7bcommand,
                width=30,
                height=8)
c.pack(side=LEFT)

d = Button(root, text= 'Need Help?', command=help,
                width=10,
                height=3)
d.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)


root.mainloop()