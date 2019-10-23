from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
from tkinter import messagebox

def helloCallBack():
    master2=Tk()
    frame1=Frame(master2,bd=10,height=500,padx=10,pady=10,width=1500)
    frame1.pack()
    B = Button(frame1, text ="Choose Directory")
    B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
    B.config(width=45)


master = Tk()
frame1=Frame(master,bd=10,height=500,padx=10,pady=10,width=1500)
frame1.pack()
B = Button(frame1, text ="Choose Directory", command = helloCallBack)
B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
mainloop()