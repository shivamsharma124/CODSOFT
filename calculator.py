from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.config(bg="black")
root.resizable(0,0)

# function
calc=""
def clear():
    global calc
    e.delete(0,END)
    calc=""
def press(n):
    global calc
    calc=calc+str(n)
    e.delete(0,END)
    e.insert(0,calc)
def back():
    current =e.get()
    e.delete(0,END)
    e.insert(0,current[:-1])
    global calc
    calc=current[:-1]
    
def equal ():
    global calc
    calc=str(eval(calc))
    e.delete(0,END)
    e.insert(0,calc)
    

# v=StringVar()
e=Entry(root,border=6,width=64,bg="#202020",fg="White")
e.grid(row=0,column=0,columnspan=4)
# creating button
bt_equal=Button(root,text="=",padx=88,pady=20,command=equal,bg="#202020",fg="orange")
bt_clear=Button(root,text="Clear",padx=80,pady=20,command=clear,bg="#202020",fg="White")
bt_back=Button(root,text="<",padx=40,pady=20,command=back,bg="#202020",fg="White")

bt_1=Button(root,text="1",padx=40,pady=20,command=lambda : press("1"),bg="#202020",fg="White")
bt_2=Button(root,text="2",padx=40,pady=20,command=lambda : press("2"),bg="#202020",fg="White")
bt_3=Button(root,text="3",padx=40,pady=20,command=lambda : press("3"),bg="#202020",fg="White")
bt_4=Button(root,text="4",padx=40,pady=20,command=lambda : press("4"),bg="#202020",fg="White")
bt_5=Button(root,text="5",padx=40,pady=20,command=lambda : press("5"),bg="#202020",fg="White")
bt_6=Button(root,text="6",padx=40,pady=20,command=lambda : press("6"),bg="#202020",fg="White")
bt_7=Button(root,text="7",padx=40,pady=20,command=lambda : press("7"),bg="#202020",fg="White")
bt_8=Button(root,text="8",padx=40,pady=20,command=lambda : press("8"),bg="#202020",fg="White")
bt_9=Button(root,text="9",padx=40,pady=20,command=lambda : press("9"),bg="#202020",fg="White")
bt_0=Button(root,text="0",padx=40,pady=20,command=lambda : press("0"),bg="#202020",fg="White")
bt_dot=Button(root,text=".",padx=41,pady=20,command=lambda : press("."),bg="#202020",fg="White")
bt_add=Button(root,text="+",padx=39,pady=20,command=lambda : press("+"),bg="#202020",fg="White")
bt_sub=Button(root,text="-",padx=40,pady=20,command=lambda : press("-"),bg="#202020",fg="White")
bt_div=Button(root,text="/",padx=40,pady=20,command=lambda : press("/"),bg="#202020",fg="White")
bt_mul=Button(root,text="*",padx=40,pady=20,command=lambda : press("*"),bg="#202020",fg="White")
bt_clear.grid(row=1,column=0,columnspan=2)
bt_back.grid(row=1,column=2)
bt_div.grid(row=1,column=3)
bt_9.grid(row=2,column=0)
bt_8.grid(row=2,column=1)
bt_7.grid(row=2,column=2)
bt_mul.grid(row=2,column=3)
bt_6.grid(row=3,column=0)
bt_5.grid(row=3,column=1)
bt_4.grid(row=3,column=2)
bt_sub.grid(row=3,column=3)
bt_3.grid(row=4,column=0)
bt_2.grid(row=4,column=1)
bt_1.grid(row=4,column=2)
bt_add.grid(row=4,column=3)
bt_0.grid(row=5,column=0)
bt_dot.grid(row=5,column=1)
bt_equal.grid(row=5,column=2,columnspan=2)
root.mainloop()