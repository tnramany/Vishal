from tkinter import *
from math import *

def evaluate(event):
    res.configure(text= "answer:" +str(eval(entry.get())))

window=Tk()
Label(window, text="Your Expression:").pack()


entry= Entry(window)
entry.bind("<Return>", evaluate)
entry.pack()

res= Label(window)
res.pack()