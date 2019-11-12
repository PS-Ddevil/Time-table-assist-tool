from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
import sqlite3
from PIL import ImageTk



def TimeTable1():
    os.system("python3 progs/prog1.py")
    print(os.getcwd())
def TimeTable2():
    os.system("python3 progs/func/final_time_table.py")
    print(os.getcwd())
def SlotSlection():
    os.system("python3 progs/prog2.py")
    print(os.getcwd())
def ClassSelection():
    os.system("python3 progs/prog3.py")
def Initialise():
    os.system("python3 progs/func/extract_docxs.py")
    os.system("python3 progs/func/read_create.py")
    os.system("python3 progs/func/read_create_E.py")
    os.system("python3 progs/func/extract_ods.py")
    os.system("python3 progs/func/multi_faculty.py")
master=Tk()
master.title("Main")
master.geometry("790x790+100+100")
canvas = Canvas(master,width = 200, height = 200, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = "5.png")
canvas.create_image(0, 0, image = image, anchor = NW)
B = Button(canvas, text ="Initialise",font=("Courier", 18),command = Initialise)
B.place(x=300,y=210)
B = Button(canvas, text ="Slot Selection",font=("Courier", 18), command = SlotSlection)
B.place(x=0,y=540)
B = Button(canvas, text ="Class Selection",font=("Courier", 18), command = ClassSelection)
B.place(x=280,y=540)
B = Button(canvas, text ="Time Table",font=("Courier", 18), command = TimeTable1)
B.place(x=600,y=540)
B = Button(canvas, text ="Release", font=("Courier", 18),command = TimeTable2)
B.place(x=325,y=710)

mainloop()