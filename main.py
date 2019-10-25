from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
import sqlite3
from progs.prog1 import TimeTable
from progs.prog2 import Basket

master = Tk()
master.title("Time Table Assist Tool")
frame=Frame(master,bd=10,height=500,padx=10,pady=10,width=1500)
frame.pack()
B = Button(frame, text ="Time Table", command = TimeTable)
B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
B = Button(frame, text ="BaSket", command = Basket)
B.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)

mainloop()