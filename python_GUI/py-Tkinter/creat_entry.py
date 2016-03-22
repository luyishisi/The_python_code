#coding:utf-8
from tkinter import *
root = Tk()
root.title("hello,world")
root.geometry('300x200')#是x不是*
Label(root, text='creat-entry',font=('Arial', 20)).pack()

var = StringVar()
e = Entry(root,textvariable = var)
var.set("hello")
e.pack()

root.mainloop()

