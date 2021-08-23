import tkinter

###main

window=tkinter.Tk()

window.title("My button")

button = tkinter.Button(window,text="Hi",width=40)

button.pack(padx=20,pady=20)

clickNo=0

def onClick(event):
    global clickNo
    clickNo=clickNo+1
    if clickNo==1:
        button.configure(text="Click 1")
    elif clickNo==2:
        button.configure(text="Click 2")
    else:
        button.pack_forget()





button.bind("<ButtonRelease-1>",onClick)

window.mainloop()