#coding:utf-8
from tkinter import *
import time
root = Tk()
root.title("hello,world")
root.geometry('300x200')#是x不是*
root.resizable(width=False, height=True)
Label(root, text='creat-text',font=('Arial', 20)).pack()

t = Text(root)
t.pack()
t.insert(1.0,'hello\n')
t.insert(END,'hello111\n')
t.insert(END,'hello222')
t.insert(END,'hello333\n')
root.mainloop()

