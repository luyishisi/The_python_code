#python tkinter image

from tkinter import *


def main():
    filename =r'./1.gif'
    root = Tk()
    img = PhotoImage(file=filename)
    label = Label(root, image=img)
    label.pack()
    root.mainloop()

main()
