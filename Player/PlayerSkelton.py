import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import dialog
from tkinter import ttk
from tkinter import filedialog
from pygame import mixer
class player:
    isloaded = True
    def __init__(self, window):
        #initialzing main window
        self.window = window
        window.geometry('500x200'); window.title('Player')
        window.resizable(300,200)
        Load = Button(window,text='Load',width=10,font=('Times',10),command = self.load,foreground="blue")
        Load.flash()
        play = Button(window,text = 'Play',width=10,font=('Times',10),command=self.play,foreground="purple")
        Stop = Button(window,text='Stop',width=10,font=('Times',10),command=self.stop,foreground="red")
        Pause = Button(window,text='Pause',width=10,font=('Times',10),command=self.Pause,foreground="yellow")
        Load.place(x = 0,y = 10)
        play.place(x = 90,y = 10)
        Stop.place(x = 0, y = 40)
        Pause.place(x = 90,y =40)
        self.music_file = False
        self.music_f = ""
        self.playing = False

    def load(self):
        self.music_file = filedialog.askopenfile()
        self.music_f = str(self.music_file)
        # print(self.music_file)
    def play(self):
        try:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
        except :
            Tk.geometry(self.window)
    def getfile(self):
        return self.music_f
    def stop(self):
       if not self.playing:
        mixer.music.stop()
        self.playing = True
       else:
        mixer.music.play()
        self.playing = False
    def Pause(self):
        if not self.playing:
            mixer.music.pause()
            self.playing = True
        else:
            mixer.music.unpause()
            self.playing = False
