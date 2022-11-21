from imp import reload
import os
import subprocess
from sys import stderr, stdout
import tkinter
from webbrowser import get
import pywintypes
import win32api
import win32con
from tkinter import *
class Setting:
    def __init__(self,window):
        self.window = window;
        self.window.geometry('500x200')
        self.window.title('Setting Manger')
        load = Button(self.window,text="Change Res",command=self.changeRes,bg="blue")
        load.place(x=10,y=30)
        getDir = Button(self.window,text="Show Dir",command=self.startCmd,bg="yellow")
        getDir.place(x=20,y=60)

    def changeRes(self):
        py = pywintypes.DEVMODEType()
        py.PelsWidth  = 1680
        py.PelsHeight = 1050
        py.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        win32api.ChangeDisplaySettings(py,0)

    def computerName(self):
        text = Text(self.window,width=20,height=2)
        currRes = win32api.GetComputerName()
        text.insert(tkinter.END,currRes)
        text.pack()

    def startCmd(self):
        process = subprocess.Popen('dir',shell=True)
        
        






