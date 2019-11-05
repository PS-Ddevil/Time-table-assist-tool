from tkinter import *
from tkinter import messagebox
import os
from func.save import save_in_excel_sheet
from func.undo import undo_in_excel_sheet
from func.initialize_excel_files import slot
from time import sleep
from tkinter import *
from PIL import ImageTk, Image

master = Tk()
master.title("Time table assist tool")

# DEFINING THE GUI ELEMENTS
img=Image.open("./src/logo/iitmandilogo.jpg")
img = ImageTk.PhotoImage(img)
label = Label(image=img)
label.grid(row=0,column=0)
Label(master,width=14,height=2, text='8:00 - 8:50', relief="solid",bg='red').grid(row=0,column=1)
Label(master,width=14,height=2, text='9:00 - 9:51', relief="solid",bg='pink').grid(row=0,column=2)
Label(master,width=14,height=2, text='10:00 - 10:50', relief="solid",bg='yellow').grid(row=0,column=3)
Label(master,width=14,height=2, text='11:00 - 11:50', relief="solid",bg='orange').grid(row=0,column=4)
Label(master,width=14,height=2, text='LUNCH BREAK', relief="solid").grid(row=0,column=5, rowspan=5)
Label(master,width=14,height=2, text='1:00 - 1:50', relief="solid",bg='blue').grid(row=0,column=6)
Label(master,width=14,height=2, text='2:00 - 2:50', relief="solid",bg='pink').grid(row=0,column=7)
Label(master,width=14,height=2, text='3:00 - 3:50', relief="solid",bg='green').grid(row=0,column=8)
Label(master,width=14,height=2, text='4:00 - 4:50', relief="solid",bg='red').grid(row=0,column=9)
Label(master,width=14,height=2, text='Monday', relief="solid",bg='red').grid(row=1)
Label(master,width=14,height=2, text='Tuesday', relief="solid",bg='blue').grid(row=2)
Label(master,width=14,height=2, text='Wednesday', relief="solid",bg='green').grid(row=3)
Label(master,width=14,height=2, text='Thrusday', relief="solid",bg='yellow').grid(row=4)
Label(master,width=14,height=2, text='Friday', relief="solid",bg='pink').grid(row=5)

Course_Dict = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4}
left_course = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	# THIS SECTION DEFINES THE ALGORITHM TO UPDATE THE OPTIONS IN THE GUI
def update_options(var, row_val):
	cr = cr_vars[var].get()
	if cr=='SLOT':
		return
	if(old_var[var] == cr):
		return 0
	if match[row_val][ord(cr)-65] == True:
		for i in range(((row_val-1)*9),((row_val-1)*9)+9):
			if cr_vars[i].get()==cr_vars[var].get():
				w = OptionMenu(master, cr_vars[i], *left_course)
				w.config(width=10,height=2,bg='red')
				w.grid(row=row_val,column=(i%9)+1)
		messagebox.showerror("Error", "More than one occurance of a slot on same day")
		cr_vars[var].set("SLOT")
		for i in range(((row_val-1)*9),((row_val-1)*9)+9):
			if i!=((row_val-1)*9)+4:
				w = OptionMenu(master, cr_vars[i], *left_course)
				w.config(width=10,height=2,bg='lightgray')
				w.grid(row=row_val,column=(i%9)+1)


		return 0
	match[row_val][ord(cr)-65] = True
	Course_Dict[cr] -= 1
	if old_var[var] != "SLOT":
		Course_Dict[old_var[var]] += 1
		match[row_val][ord(old_var[var])-65] = False
	old_var[var] = cr
	if(Course_Dict[cr] < 0):
		for i in range(0,45):
			if cr_vars[var].get()==cr_vars[i].get():
				w = OptionMenu(master, cr_vars[i], *left_course)
				w.config(width=10,height=2,bg='red')
				w.grid(row=int(i/9)+1,column=(i%9)+1)

		messagebox.showerror("Error", "More than required slots")
		cr_vars[var].set("SLOT")

		for i in range(0,45):
			if (i%9)!=4:
				w = OptionMenu(master, cr_vars[i], *left_course)
				w.config(width=10,height=2,bg='lightgray')
				w.grid(row=int(i/9)+1,column=(i%9)+1)

		Course_Dict[cr] += 1

cr_vars = []
old_var = []
z = 0
match = [[False for i in range(8)] for j in range(6)]
# THIS SECTION DEFINES THE RENDERING OF THE SLOTS IN THE GUI'S TIMETABLE MATRIX
for i in range(1,6):
	for j in range(1,10):
		cr_vars.append(StringVar(master))
		cr_vars[z].set("SLOT")
		old_var.append("SLOT")
		w = OptionMenu(master, cr_vars[z], *left_course)
		w.config(width=10,height=2)
		if(j != 5):
			w.grid(row=i,column=j)
		cr_vars[z].trace("w", lambda *_, var=z, row_val=i: update_options(var, row_val))
		z = z + 1

Label(master, text='\n').grid(row=7)
button = Button(master, text='Undo',activeforeground='blue',activebackground='red', command=lambda: undo_in_excel_sheet(cr_vars))
button.grid(row=8,column=3)
button = Button(master, text='Save',activeforeground='blue',activebackground='red', command=lambda: save_in_excel_sheet(cr_vars))
button.grid(row=8,column=5)
slot()
mainloop()