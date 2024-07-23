from tkinter import *
from random import randint
root=Tk()
def gen ():
    l=int(length.get())
    p=[]
    for i in range(0,l):
        a=chr(randint(33,126))
        p.append(a)
    pw.delete(0,END)
    pw.insert(0,p)
def copy():
    root.clipboard_clear()
    root.clipboard_append(pw.get())
root.geometry("500x300")
entry_frame=LabelFrame(root,text="Enter the length of the password")
entry_frame.pack(pady=20)
length=Entry(entry_frame,font=("Helvetica",24))
length.pack(pady=20)
pw=Entry(root,text='',font=("Helvetica",24),border=0,bg="systembuttonface")
pw.pack(pady=(0,20))
fun_frame=Frame(root)
fun_frame.pack(pady=20)
G_bt=Button(fun_frame,text="Generate password",command=gen)
G_bt.grid(row=0,column=0,padx=20)
c_bt=Button(fun_frame,text="Copy to clipboard",command=copy)
c_bt.grid(row=0,column=1)
root.mainloop()
