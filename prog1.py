from tkinter import *
from tkinter import messagebox
import save as s
import undo as u
import initialize_excel_files
initialize_excel_files.slot()
master = Tk()
master.title("Time table assist tool")

# DEFINING THE GUI ELEMENTS
<<<<<<< HEAD
Label(master,width=20,height=2, text='').grid(row=0) 
Label(master,width=20,height=2, text='8:00 - 8:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=1) 
Label(master,width=20,height=2, text='9:00 - 9:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=2) 
Label(master,width=20,height=2, text='10:00 - 10:50',borderwidth=2, relief="solid",bg='yellow').grid(row=0,column=3) 
Label(master,width=20,height=2, text='11:00 - 11:50',borderwidth=2, relief="solid",bg='orange').grid(row=0,column=4) 
Label(master,width=20,height=2, text='LUNCH BREAK',borderwidth=2, relief="solid").grid(row=0,column=5, rowspan=5)
Label(master,width=20,height=2, text='1:00 - 1:50',borderwidth=2, relief="solid",bg='blue').grid(row=0,column=6) 
Label(master,width=20,height=2, text='2:00 - 2:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=7) 
Label(master,width=20,height=2, text='3:00 - 3:50',borderwidth=2, relief="solid",bg='green').grid(row=0,column=8) 
Label(master,width=20,height=2, text='4:00 - 4:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=9) 
Label(master,width=20,height=2, text='Monday',borderwidth=2, relief="solid",bg='red').grid(row=1) 
Label(master,width=20,height=2, text='Tuesday',borderwidth=2, relief="solid",bg='blue').grid(row=2) 
Label(master,width=20,height=2, text='Wednesday',borderwidth=2, relief="solid",bg='green').grid(row=3) 
Label(master,width=20,height=2, text='Thrusday',borderwidth=2, relief="solid",bg='yellow').grid(row=4) 
Label(master,width=20,height=2, text='Friday',borderwidth=2, relief="solid",bg='pink').grid(row=5) 
=======
Label(master, text='').grid(row=0)
Label(master, text='8:00 - 8:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=1)
Label(master, text='9:00 - 9:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=2)
Label(master, text='10:00 - 10:50',borderwidth=2, relief="solid",bg='yellow').grid(row=0,column=3)
Label(master, text='11:00 - 11:50',borderwidth=2, relief="solid",bg='orange').grid(row=0,column=4)
Label(master, text='LUNCH BREAK',borderwidth=2, relief="solid").grid(row=0,column=5, rowspan=5)
Label(master, text='1:00 - 1:50',borderwidth=2, relief="solid",bg='blue').grid(row=0,column=6)
Label(master, text='2:00 - 2:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=7)
Label(master, text='3:00 - 3:50',borderwidth=2, relief="solid",bg='green').grid(row=0,column=8)
Label(master, text='4:00 - 4:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=9)
Label(master, text='Monday',borderwidth=2, relief="solid",bg='red').grid(row=1)
Label(master, text='Tuesday',borderwidth=2, relief="solid",bg='blue').grid(row=2)
Label(master, text='Wednesday',borderwidth=2, relief="solid",bg='green').grid(row=3)
Label(master, text='Thrusday',borderwidth=2, relief="solid",bg='yellow').grid(row=4)
Label(master, text='Friday',borderwidth=2, relief="solid",bg='pink').grid(row=5)
>>>>>>> upstream/master

Course_Dict = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4}

# THIS SECTION DEFINES THE ALGORITHM TO UPDATE THE OPTIONS IN THE GUI
def update_options(var, row_val):
	cr = cr_vars[var].get()
	if cr=='SLOT':
		return
	if(old_var[var] == cr):
		return 0
	if match[row_val][ord(cr)-65] == True:
		cr_vars[var].set("SLOT")
		messagebox.showerror("Error", "More than one occurance of a slot on same day")
		return 0
	match[row_val][ord(cr)-65] = True
	Course_Dict[cr] -= 1
	if old_var[var] != "SLOT":
		Course_Dict[old_var[var]] += 1
		match[row_val][ord(old_var[var])-65] = False
	old_var[var] = cr
	if(Course_Dict[cr] < 0):
		cr_vars[var].set("SLOT")
		Course_Dict[cr] += 1
		messagebox.showerror("Error", "More than required slots")

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
        left_course = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        w = OptionMenu(master, cr_vars[z], *left_course)
        w.config(width=15,height=2)
        if(j != 5):
        	w.grid(row=i,column=j)
        cr_vars[z].trace("w", lambda *_, var=z, row_val=i: update_options(var, row_val))
        z = z + 1

Label(master, text='\n').grid(row=7)
button = Button(master, text='Undo',activeforeground='blue',activebackground='red', command=lambda: u.undo_in_excel_sheet(cr_vars))
button.grid(row=8,column=3)
button = Button(master, text='Save',activeforeground='blue',activebackground='red', command=lambda: s.save_in_excel_sheet(old_var))
button.grid(row=8,column=5)
# print(len(cr_vars))
# print(old_var)

mainloop()
