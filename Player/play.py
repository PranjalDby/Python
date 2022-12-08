from tkinter import Message
from Player.PlayerSkelton import player
from tkinter import Tk
print("THIS PLAYER IS SIMPLE AND EASY TO USE")
root =Tk()
play = player(root)
message = Message(root,foreground='red',text=f'FORGED IN FIRE OF LIFE....~~~~~~~~~~')
message.pack()
root.mainloop()
