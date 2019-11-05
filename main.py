from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
import sqlite3

def TimeTable():
    os.system("python3 progs/prog1.py")
    print(os.getcwd())
def SlotSlection():
    os.system("python3 progs/prog2.py")
    print(os.getcwd())
def ClassSelection():
    os.system("python3 progs/prog3.py")
def Initialise():
    os.system("python3 progs/func/extract_docxs.py")
    os.system("python3 progs/func/read_create.py")
    os.system("python3 progs/func/extract_ods.py")
    os.system("python3 progs/func/multi_faculty.py")

master = Tk()
# master.attributes("-zoomed",True)
master.title("Time Table Assist Tool")
frame=Frame(master,bd=10,height=500,padx=10,pady=10,width=1500)
frame.pack()
B = Button(frame, text ="Initialise", command = Initialise)
B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
B = Button(frame, text ="Slot Selection", command = SlotSlection)
B.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
B = Button(frame, text ="Class Selection", command = ClassSelection)
B.grid(row=2,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
B = Button(frame, text ="Time Table", command = TimeTable)
B.grid(row=3,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)

mainloop()