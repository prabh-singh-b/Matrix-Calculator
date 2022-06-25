from tkinter import *
from glbl import *

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
    global res, mat1,mat2,matwidth, operation
    operation = "+"

    for i in range(matwidth):
        row = []
        for j in range(matwidth):
            row.append(mat1[i][j] + mat2[i][j])
        res.append(row)

    Result(root)

def SUB(root):
    global res, mat1,mat2,matwidth, operation
    operation = "-"

    for i in range(matwidth):
        row = []
        for j in range(matwidth):
            row.append(mat1[i][j] - mat2[i][j])
        res.append(row)
    Result(root)

def MUL(root):
    global res, mat1,mat2,matwidth, operation
    operation = "x"

    for i in range(matwidth):
        row = []
        for j in range(matwidth):
            row.append(mat1[i][j] * mat2[i][j])
        res.append(row)
    Result(root)

def Result(root):
    root.destroy()
    global matwidth,res
    root = Tk()
    width = matwidth*30 + 50
    root.geometry('' + str(width*3) +"x" + str(width))
    root.title("Matrix Calculator")
    frame = Frame(root,relief = 'sunken', bg = "black")
    frame.pack(fill = BOTH, expand = True)
    for i in range(matwidth):
        for j in range(matwidth):
            l = Label(frame, text = str(mat1[i][j]))
            l.place(x = (j+1)*30, y = (i+1)*30)
    l = Label(frame, text = operation)
    l.place(x = width, y = width //2)
    for i in range(matwidth):
        for j in range(matwidth):
            l = Label(frame, text = str(mat2[i][j]))
            l.place(x = width + (j+1)*30, y = (i+1)*30)

    l = Label(frame, text = "=")
    l.place(x = 2*width - 25, y = width //2)

    for i in range(matwidth):
        for j in range(matwidth):
            l = Label(frame, text = str(res[i][j]))
            l.place(x = width + width + (j+1)*30, y = (i+1)*30)

    print(res)