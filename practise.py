from tkinter import *
from tkinter import messagebox
import sqlite3

db=sqlite3.connect('Time table')
cursor=db.cursor()
cursor.execute('create table if not exists subject(subject_code text primary key,subject_name text,slot_id text,FOREIGN KEY(slot_id) REFERENCES slot(slot_id))')
db.commit()
cursor.execute('create table if not exists slot(slot_id text primary key,faculty_id integer,FOREIGN KEY(faculty_id) REFERENCES faculty(facluty_id) )')
db.commit()
cursor.execute('create table if not exists faculty(faculty_id integer primary key,faculty_name text)')
db.commit()
print('All table created')
master1 = Tk() 
master1.title("Time table assist tool")

# DEFINING THE GUI ELEMENTS
Label(master1,width=20,height=2, text='').grid(row=0) 
Label(master1,width=20,height=2, text='8:00 - 8:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=1) 
Label(master1,width=20,height=2, text='9:00 - 9:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=2) 
Label(master1,width=20,height=2, text='10:00 - 10:50',borderwidth=2, relief="solid",bg='yellow').grid(row=0,column=3) 
Label(master1,width=20,height=2, text='11:00 - 11:50',borderwidth=2, relief="solid",bg='orange').grid(row=0,column=4) 
Label(master1,width=20,height=2, text='LUNCH BREAK',borderwidth=2, relief="solid").grid(row=0,column=5, rowspan=5)
Label(master1,width=20,height=2, text='1:00 - 1:50',borderwidth=2, relief="solid",bg='blue').grid(row=0,column=6) 
Label(master1,width=20,height=2, text='2:00 - 2:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=7) 
Label(master1,width=20,height=2, text='3:00 - 3:50',borderwidth=2, relief="solid",bg='green').grid(row=0,column=8) 
Label(master1,width=20,height=2, text='4:00 - 4:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=9) 
Label(master1,width=20,height=2, text='Monday',borderwidth=2, relief="solid",bg='red').grid(row=1) 
Label(master1,width=20,height=2, text='Tuesday',borderwidth=2, relief="solid",bg='blue').grid(row=2) 
Label(master1,width=20,height=2, text='Wednesday',borderwidth=2, relief="solid",bg='green').grid(row=3) 
Label(master1,width=20,height=2, text='Thrusday',borderwidth=2, relief="solid",bg='yellow').grid(row=4) 
Label(master1,width=20,height=2, text='Friday',borderwidth=2, relief="solid",bg='pink').grid(row=5) 

Course_Dict = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4} 

# THIS SECTION DEFINES THE ALGORITHM TO UPDATE THE OPTIONS IN THE GUI
def update_options(var, row_val):
	cr = cr_vars[var].get()
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
        cr_vars.append(StringVar(master1))
        cr_vars[z].set("SLOT")
        old_var.append("SLOT")
        left_course = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        w = OptionMenu(master1, cr_vars[z], *left_course)
        w.config(width=15,height=2)
        if(j != 5):
        	w.grid(row=i,column=j)
        cr_vars[z].trace("w", lambda *_, var=z, row_val=i: update_options(var, row_val))
        z = z + 1
mainloop() 
