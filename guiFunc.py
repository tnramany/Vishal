from tkinter import *

def convert_fahr():
    words=fbtext.get()
    ftemp=float(words)
    celbox.delete(0,END)
    celbox.insert(0,'%.2f'% (tocel(ftemp)))
    kelbox.delete(0,END)
    kelbox.insert(0, '%.2f'% (tokel(tocel(ftemp))))
    return

def convert_cel():
    words = cbtext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(ctemp)))

def convert_kel():
    words = kbtext.get()
    ktemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ktoc(ktemp))))
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (ktoc(ktemp)))

def tocel(fahr):
    return (fahr-32)* 5.0/9.0

def tofahr(cel):
    return cel* 9.0/5.0+ 32

def ktoc(kel):
    return kel - 273.15

def tokel(cel):
    return cel+ 273.15

w=Tk()

w.title("My temperature converter")


fahrlabel = Label(w,text = 'Fahrenheit:')
fahrlabel.grid(row =0, column=0,padx=5,pady=5,sticky= E)

cellabel = Label(w,text = 'Celsius:')
cellabel.grid(row = 1, column = 0, padx = 5,pady = 5, sticky = E)

kellabel = Label(w,text = 'Kelvin:')
kellabel.grid(row = 2, column = 0, padx = 5,pady = 5, sticky = E)


fbtext = StringVar()
fbtext.set('')
fahrbox = Entry(w,textvariable=fbtext)
fahrbox.grid(row=0,column=1,padx=5,pady=5)

cbtext = StringVar()
cbtext.set('')
celbox = Entry(w,textvariable=cbtext)
celbox.grid(row=1,column=1,padx=5,pady=5)

kbtext = StringVar()
kbtext.set('')
kelbox = Entry(w,textvariable=kbtext)
kelbox.grid(row=2,column=1,padx=5,pady=5)



fgobutton = Button(w,text = 'Go',command = convert_fahr)

fgobutton.grid(row = 0,column = 2,padx = 5,pady= 5,sticky=N+S+E+W)

cgobutton = Button(w,text = 'Go',command = convert_cel)

cgobutton.grid(row = 1,column = 2,padx = 5,pady= 5,sticky=N+S+E+W)

kgobutton = Button(w,text = 'Go',command = convert_kel)

kgobutton.grid(row = 2,column = 2,padx = 5,pady= 5,sticky=N+S+E+W)

exitbutton = Button(w, text = 'Exit', command = quit)

exitbutton.grid(row=3, column=0, padx= 5, pady= 5, sticky= N+S+E+W, columnspan= 3)





w.mainloop()