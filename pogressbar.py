import tkinter 
from tkinter import *
from tkinter.tix import TEXT
from tkinter.ttk import Progressbar

root = Tk()

progress = Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')

def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 70
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 90
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

progress.pack(pady=10)
Button(root,text="Start",command=bar).pack(pady=10)

mainloop()


