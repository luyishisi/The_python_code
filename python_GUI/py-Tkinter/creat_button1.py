# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
root.title("hello world")
root.geometry()

def printhello():
    t.insert('1.0', "hello\n")
    
t = Text()
t.pack()
Button(root, text="press", command = printhello).pack()
root.mainloop()
