import subprocess
from tkinter import *
import os
import guidef as gd
import turtle

try:
    root = Tk()
    root.title("Self Driving Car") #title of window
    root.geometry('500x300') #size of the window
    root['background'] = "#16a11b" #background color of window


    pick = Label(root, text="Pick a map", bg='#16a11b')#The label for Pick a map
    pick.place(x=207, y= 75)#the position of label

    butt1 = Button(root, text='Map 1',fg="black",bg = '#c12111', width=10,height=5, command=gd.firstbutt)
    butt1.place(x=120, y=100)#the first button for map 1 it can be clicked and uses the function to open the first map file
    #position of button 1

    butt2 = Button(root, text='Map 2',fg="black",bg = '#c12111', width=10,height=5, command=gd.secbutt)
    butt2.place(x=200, y=100)#the second button for map 2 it can be clicked and uses the function to open the second map file
    #position of button 2

    butt3 = Button(root, text='Map 3',fg="black",bg = '#c12111', width=10,height=5, command=gd.thirdbutt)
    butt3.place(x=280, y=100)#the first button for map 3 it can be clicked and uses the function to open the third map file
    #position of button 3

    root.mainloop()
except:
    exitcode()

