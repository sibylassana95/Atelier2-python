import tkinter
from tkinter import messagebox

gui = tkinter.Tk()

def msgCallBack():
   messagebox.showinfo("Bienvenue")

btn = tkinter.Button(gui, text ="Cliquez ici!", command = msgCallBack)

btn.pack()
gui.mainloop()
