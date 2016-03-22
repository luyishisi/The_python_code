#coding:utf-8
from tkinter import *
root = Tk()
root.title("hello,world")
#root.geometry('300x200')#是x不是*
#root.resizable(width=False, height=True)
Label(root, text='caret-button',font=('Arial', 20)).pack()
temp = 0;


def printhello():
    t.insert('1.0','123123\n')

filepwd = '1.gif'
img = PhotoImage(file=filepwd)
label = Label(root,image=img)
label.pack()

t = Text()
t.pack()

Button(root,text="press",command = printhello).pack()

root.mainloop()

