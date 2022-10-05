from tkinter import ttk
from tokenize import Double
from PlayerSkelton import *
from tkinter import *
print("THIS PLAYER IS SIMPLE AND EASY TO USE")
root =Tk()
message = Message(root,foreground='red',text="HELLO WELCOME TO MY SIMPLE MUSIC PLAYER")
message.pack()
play = player(root)
root.mainloop()
