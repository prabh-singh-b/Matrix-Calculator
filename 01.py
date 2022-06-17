from cgitb import reset
from tkinter import *
from tkinter import ttk

mat1 = []
mat2 = []
matwidth = 4
cur_row = 1
cur_mat = 1
res = []

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

def data(root, opr): 
    #opr is operation
    root.destroy()
    root = Tk()
    root.geometry('500x300')
    root.title("Matrix Calculator")

    frame= Frame(root,relief = 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True)

    global mat1
    global mat2
    global matwidth, cur_row, cur_mat

    l1 = Label(frame, text = "Enter Values for matrix 1", fg = "white", bg = "black")
    l2 = Label(frame, text = "Enter Values for row 1", fg = "white", bg = "black")
    
    l1wid = l1.winfo_reqwidth()//2
    l2wid = l2.winfo_reqwidth()//2
    l1.place(x = 250 - l1wid, y = 30)
    l2.place(x = 10, y = 80)

    en = Entry(frame, width = 25)
    en.place(x = (l2wid*2) + 50, y = 80)

    b1 = Button(frame, width = 10, text = "NEXT", command = lambda : inp(en,l1,l2,opr,root))
    b1.place(x = (375), y = 80)
    


    mainloop()

    
def inp(en,l1,l2,opr,root):
    row = list(map(lambda x: int(x),en.get().split()))
    global cur_mat, cur_row, matwidth, mat1, mat2
    en.delete(0,END)
    if(len(row) > matwidth):
        return
    elif(len(row) < matwidth):
        for i in range(matwidth - len(row)):
            row.append(0)
    if(cur_mat == 1): mat1.append(row)
    else: mat2.append(row)

    
    print(mat1, mat2,cur_mat,cur_row)

    if(cur_row == matwidth):
        if(cur_mat == 1):
            cur_row = 1
            cur_mat = 2
            l1.config(text = "Enter Values for matrix 2")
        # else implement a function for when both the matrices are filled
        else:
            if( opr == "add"):
                ADD(root)
                return
            elif(opr == "sub"):
                SUB(root)
            elif(opr == "mul"):
                MUL(root)
    else: cur_row += 1

    l2.config(text = "Enter Values for row "+str(cur_row))


def ADD(root):
    global res, mat1,mat2,matwidth

    for i in range(matwidth):
        row = []
        for j in range(matwidth):
            row.append(mat1[i][j] + mat2[i][j])
        res.append(row)

    Result(root)

def Result(root):
    root.destroy()
    global matwidth,res
    root = Tk()
    width = matwidth*30 + 50
    root.geometry('' + str(width) +"x" + str(width))
    root.title("Matrix Calculator")
    frame = Frame(root,relief = 'sunken', bg = "black")
    frame.pack(fill = BOTH, expand = True)
    for i in range(matwidth):
        for j in range(matwidth):
            l = Label(frame, text = str(res[i][j]))
            l.place(x = (j+1)*30, y = (i+1)*30)

    print(res)

def SUB(root):
    global res, mat1,mat2,matwidth
    for i in range(matwidth):
        row = []
        for j in range(matwidth):
            row.append(mat1[i][j] - mat2[i][j])
        res.append(row)
    Result(root)

def MUL(root):
    global res, mat1,mat2,matwidth
    for i in range(matwidth):
        row = []
        for j in range(matwidth):
            row.append(mat1[i][j] * mat2[i][j])
        res.append(row)
    Result(root)

mainMenu()