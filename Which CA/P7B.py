from audioop import mul
from cgi import test
from doctest import OutputChecker
from importlib.resources import path
from pydoc import text
import subprocess
from tkinter.tix import Tk
from typing_extensions import IntVar
from unicodedata import name
from click import command
from _tkinter import *
import tkinter as tk
from numpy import empty
import pyperclip as pc
import time
from pynput.keyboard import Key, Controller
import re
import Variable
from calendar import c
import pyperclip as pc
  
root = tk.Tk()
root.title("Path Input")
root.geometry('400x290')

#Command for Enter Path Button
def EnterPath():
    inp = inputtxt.get("1.0", "end-1c")
    lbl.config(text = "Provided Input: "+inp)
    nameoffile = inp

    disallowedcharacters = '"'
    for character in disallowedcharacters: 
        nameoffile = nameoffile.replace(character,"")
    
    newname = nameoffile

    newname = re.sub('.p7b', '', newname)

    txtline2 = f'pkcs7 -print_certs -in "{nameoffile}" -out "{newname}.pem"'

    file = open('post.txt', 'w')
    lines = [txtline2]
    with open('post.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')

#Command for 2 Sets of Certificates
def box2command():
    inp = inputtxt.get("1.0", "end-1c")
    lbl.config(text = "Provided Input: "+inp)
    file = inp.replace('"', "")


    fileout1 = 'CAfile1.p7b'
    fileout2 = 'CAfile2.p7b'
    fileout3 = 'CAfile3.p7b'

    with open(file) as infile, open(fileout1, 'w') as outfile, open(fileout2, 'w') as outfile2, open(fileout3, 'w') as outfile3:
        copy = False
        counter = 0
        for line in infile:
            if counter == 0:
                if line.strip() == "-----BEGIN CERTIFICATE-----":
                    copy = True
                    continue
                elif line.strip() == "-----END CERTIFICATE-----":
                    copy = False
                    counter = 1
                    continue
                elif copy:
                    outfile.write(line)
            if counter == 1:
                if line.strip() == "-----BEGIN CERTIFICATE-----":
                    copy = True
                    continue
                elif line.strip() == "-----END CERTIFICATE-----":
                    copy = False
                    counter = 2
                    continue
                elif copy:
                    outfile2.write(line)
    #CAfile1 REWRITE
    with open('CAfile1.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile1.p7b', "w+") as f: 
            f.write("-----BEGIN CERTIFICATE-----")
            f.write('\n')
            f.write(a)
            with open('CAfile1.p7b', "r+") as f: 
                b = f.read() 
    with open('CAfile1.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile1.p7b', "w+") as f: 
            f.write(a)
            f.write("-----END CERTIFICATE-----")
            with open('CAfile1.p7b', "r+") as f: 
                b = f.read() 

    #CAfile2 REWRITE
    with open('CAfile2.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile2.p7b', "w+") as f: 
            f.write("-----BEGIN CERTIFICATE-----")
            f.write('\n')
            f.write(a)
            with open('CAfile2.p7b', "r+") as f: 
                b = f.read() 
    with open('CAfile2.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile2.p7b', "w+") as f: 
            f.write(a)
            f.write("-----END CERTIFICATE-----")
            with open('CAfile2.p7b', "r+") as f: 
                b = f.read() 

    #CAfile 1 + 2 input CMD           
    output1 = Variable.p7bCAfile1path
    output1 = re.sub('.p7b', '', output1)
    codecontent1 = f'pkcs7 -print_certs -in "{Variable.p7bCAfile1path}" -out "{output1}.pem"'
    pc.copy(codecontent1)
    function = Variable.path
    subprocess.Popen(["start", "cmd", "/k", function], shell = True)
    keyboard = Controller()
    time.sleep(2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    output2 = Variable.p7bCAfile2path
    output2 = re.sub('.p7b', '', output2)
    codecontent2 = f'pkcs7 -print_certs -in "{Variable.p7bCAfile2path}" -out "{output2}.pem"'
    pc.copy(codecontent2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(2)
    keyboard.press(Key.enter)

#Command for 3 sets of Certificates
def box3command():
    inp = inputtxt.get("1.0", "end-1c")
    lbl.config(text = "Provided Input: "+inp)
    file = inp.replace('"', "")
    fileout1 = 'CAfile1.p7b'
    fileout2 = 'CAfile2.p7b'
    fileout3 = 'CAfile3.p7b'

    with open(file) as infile, open(fileout1, 'w') as outfile, open(fileout2, 'w') as outfile2, open(fileout3, 'w') as outfile3:
            copy = False
            counter = 0
            for line in infile:
                if counter == 0:
                    if line.strip() == "-----BEGIN CERTIFICATE-----":
                        copy = True
                        continue
                    elif line.strip() == "-----END CERTIFICATE-----":
                        copy = False
                        counter = 1
                        continue
                    elif copy:
                        outfile.write(line)
                if counter == 1:
                    if line.strip() == "-----BEGIN CERTIFICATE-----":
                        copy = True
                        continue
                    elif line.strip() == "-----END CERTIFICATE-----":
                        copy = False
                        counter = 2
                        continue
                    elif copy:
                        outfile2.write(line)
                if counter == 2:
                    if line.strip() == "-----BEGIN CERTIFICATE-----":
                        copy = True
                        continue
                    elif line.strip() == "-----END CERTIFICATE-----":
                        copy = False
                        continue
                    elif copy:
                        outfile3.write(line)
    #CAfile1 REWRITE
    with open('CAfile1.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile1.p7b', "w+") as f: 
            f.write("-----BEGIN CERTIFICATE-----")
            f.write('\n')
            f.write(a)
            with open('CAfile1.p7b', "r+") as f: 
                b = f.read() 
    with open('CAfile1.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile1.p7b', "w+") as f: 
            f.write(a)
            f.write("-----END CERTIFICATE-----")
            with open('CAfile1.p7b', "r+") as f: 
                b = f.read() 
    #CAfile2 REWRITE
    with open('CAfile2.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile2.p7b', "w+") as f: 
            f.write("-----BEGIN CERTIFICATE-----")
            f.write('\n')
            f.write(a)
            with open('CAfile2.p7b', "r+") as f: 
                b = f.read() 
    with open('CAfile2.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile2.p7b', "w+") as f: 
            f.write(a)
            f.write("-----END CERTIFICATE-----")
            with open('CAfile2.p7b', "r+") as f: 
                b = f.read() 
    #CAfile3 REWRITE
    with open('CAfile3.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile3.p7b', "w+") as f: 
            f.write("-----BEGIN CERTIFICATE-----")
            f.write('\n')
            f.write(a)
            with open('CAfile3.p7b', "r+") as f: 
                b = f.read() 
    with open('CAfile3.p7b', "r+") as f: 
        a = f.read() 
        with open('CAfile3.p7b', "w+") as f: 
            f.write(a)
            f.write("-----END CERTIFICATE-----")
            with open('CAfile3.p7b', "r+") as f: 
                b = f.read() 
                
    #CAfile 1 + 2 + 3 input CMD           
    output1 = Variable.p7bCAfile1path
    output1 = re.sub('.p7b', '', output1)
    codecontent1 = f'pkcs7 -print_certs -in "{Variable.p7bCAfile1path}" -out "{output1}.pem"'
    pc.copy(codecontent1)
    function = Variable.path
    subprocess.Popen(["start", "cmd", "/k", function], shell = True)
    keyboard = Controller()
    time.sleep(2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    output2 = Variable.p7bCAfile2path
    output2 = re.sub('.p7b', '', output2)
    codecontent2 = f'pkcs7 -print_certs -in "{Variable.p7bCAfile2path}" -out "{output2}.pem"'
    pc.copy(codecontent2)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(2)
    keyboard.press(Key.enter)
    time.sleep(2)
    output3 = Variable.p7bCAfile3path
    output3 = re.sub('.p7b', '', output3)
    codecontent3 = f'pkcs7 -print_certs -in "{Variable.p7bCAfile3path}" -out "{output3}.pem"'
    pc.copy(codecontent3)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(2)
    keyboard.press(Key.enter)

#Command for CMD Execution + TXT FIle Execution + TXT Copy + TXT Paste + CMD Close
def CommandPrompt():
    function = Variable.path
    subprocess.Popen(["start", "cmd", "/k", function], shell = True)
    file = open('post.txt')
    search_word = 'pkcs7'
    with open('post.txt') as f:
        if search_word in f.read():
            print('CMD Code Found')
        else:
            print('CMD Code Not Found')
    line_number = ''
    a_file = open('post.txt')
    for number, line in enumerate(a_file):
        if search_word in line:
            line_number = number
            print(number)
            break
    codenumber = line_number
    file = open('post.txt')
    content = file.readlines()
    codecontent = content[codenumber]
    pc.copy(codecontent)
    print(codecontent)
    time.sleep(1)
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(4)
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)
    root.destroy() 


#Top Label
l = tk.Label(root, text='Type in the path to the .p7b Certificate')
l.pack()

# TextBox
inputtxt = tk.Text(root,
                   height = 5,
                   width = 20)
inputtxt.pack()

# Enter Path
printButton = tk.Button(root,
                        text = "Enter Path", 
                        command = EnterPath)
printButton.pack()

# Bottom Path Label
lbl = tk.Label(root, text = "")
lbl.pack()

#Empty Label
empty1 = tk.Label(root, text='')
empty1.pack()

#CMD Button
cmdbutton = tk.Button(root,
                        text = "One block in CA", 
                        command = CommandPrompt)
cmdbutton.pack()

#Box 2
box2 = tk.Button(root, text = "Two blocks in CA", command=box2command)
box2.pack()

#Box 3
box3 = tk.Button(root, text = "Three blocks in CA", command=box3command)
box3.pack()

root.mainloop()