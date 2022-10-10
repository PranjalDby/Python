from tkinter import Message
from PlayerSkelton import player
from tkinter import Tk
print("THIS PLAYER IS SIMPLE AND EASY TO USE")
root =Tk()
play = player(root)
message = Message(root,foreground='red',text=f'FORGED IN LIFE POWER ')
message.pack()
root.mainloop()
