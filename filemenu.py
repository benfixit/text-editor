#!/usr/bin/python3
from tkinter import *


def new_file():
    print("This is a new File!")
    return


def open_file():
    print("I need to device means on how to make more ")
    return


def save_file():
    text_input = textEditor.get("1.0", "end-1c")
    fo = open("w+", "new.txt")
    fo.write(text_input)
    fo.close()
    return


root = Tk()
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Exit", command=root.quit)
fileMenu.add_separator()

menu.add_cascade(label="File", menu=fileMenu)

editMenu = Menu(menu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

menu.add_cascade(label="Edit", menu=editMenu)

frame = Frame(root)
frame.pack()

textEditor = Text(frame, bg="#ffffff")
textEditor.pack()

root.mainloop()

