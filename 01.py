from tkinter import *
from tkinter import ttk

def mainMenu():
    root = Tk()
    root.geometry('500x300')
    root.title("Matrix Calculator")
    
    frame= Frame(root,relief = 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True)

    t = Label(frame, text = "Matrix Calculator", fg ="white", bg = "black")
    add = Button(frame, width = 10, text = "ADD")
    sub = Button(frame, width = 10, text = "SUB")
    mul = Button(frame, width = 10, text = "MUL")
    twid = t.winfo_reqwidth()//2
    addwid = add.winfo_reqwidth()//2
    subwid = sub.winfo_reqwidth()//2
    mulwid = mul.winfo_reqwidth()//2

    t.place(x = 250 - twid, y = 30)
    add.place(x = 125 - addwid, y = 60 )
    sub.place(x = 250 - subwid, y = 60)
    mul.place(x = 375 - mulwid, y = 60)
    
    root.mainloop()


mainMenu()