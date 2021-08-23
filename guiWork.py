import tkinter

window=tkinter.Tk()

window.title("My GUI")

tkinter.Label(window,text="Enter text:").grid(row=0,column=0)

entry=tkinter.Entry(window,width=20,bg="pink")
entry.grid(row=1,column=0)

tkinter.Checkbutton(window,text="Checkbutton 1").grid(row=3,column=0)
tkinter.Checkbutton(window,text="Checkbutton 2").grid(row=4,column=0)

tkinter.Scale(window,from_=0,to=100,orient=tkinter.HORIZONTAL).grid(row=4,column=1)

tkinter.Canvas(window,bg="dark blue",width=150,height=100).grid(row=4,column=2)




window.mainloop()