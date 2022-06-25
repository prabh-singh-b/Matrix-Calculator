from tkinter import *
from tkinter import ttk
from funcs import *
from glbl import *


def mainMenu():
    root = Tk()
    root.geometry('500x300')
    root.title("Matrix Calculator")
    
    frame= Frame(root,relief = 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True)

    t = Label(frame, text = "Matrix Calculator", fg ="white", bg = "black")
    add = Button(frame, width = 10, text = "ADD", command = lambda : data(root,"add"))
    sub = Button(frame, width = 10, text = "SUB", command = lambda : data(root,"sub"))
    mul = Button(frame, width = 10, text = "MUL", command = lambda : data(root,"mul"))
    twid = t.winfo_reqwidth()//2
    addwid = add.winfo_reqwidth()//2
    subwid = sub.winfo_reqwidth()//2
    mulwid = mul.winfo_reqwidth()//2

    t.place(x = 250 - twid, y = 30)
    add.place(x = 125 - addwid, y = 60 )
    sub.place(x = 250 - subwid, y = 60)
    mul.place(x = 375 - mulwid, y = 60)
    mainloop()


mainMenu()