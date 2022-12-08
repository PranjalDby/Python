from time import sleep
import tkinter
from tkinter import Button, Label, Text, Tk, filedialog
window= Tk()
text = Text(height=50,width=500,borderwidth=2,relief="solid")
def browseFile():
    filename=filedialog.askopenfile(initialdir="/Downloads",title="select a File")
    with open(filename.name,'r') as file:
        text.insert(tkinter.END,file.read(100000))
        file.close()
    button = Button(window,text="Clear",command=clearText)
    button.pack()
    text.pack()
def clearText():
    text.delete(tkinter.END,"end")
    text.pack()
button = Button(window,text="Press The Button To open The File",command=browseFile)
button.pack()
window.geometry("500x500")
window.mainloop()
