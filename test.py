from tkinter import *
from tkinter import ttk
from InitTrackerClasses import creature

cre1 = creature(player=True,name="greif1",tag="enemy",initiative="23",hp=0,maxhp="65")
cre2 = creature(player=True,name="greif2",tag="enemy",initiative="23",hp=0,maxhp="65")

tracker = [cre1, cre2]

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="", command=root.destroy).grid(column=1, row=0)
root.mainloop()