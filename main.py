from tkinter import *
from tkinter import messagebox
import sqlite3
db=sqlite3.connect('Time table')
cursor=db.cursor();
cursor.execute('create table if not exists subject(subject_code text primary key,subject_name text,slot_id text,FOREIGN KEY(slot_id) REFERENCES slot(slot_id))')
db.commit();
cursor.execute('create table if not exists slot(slot_id text primary key,faculty_id integer,FOREIGN KEY(faculty_id) REFERENCES faculty(facluty_id) )')
db.commit();
cursor.execute('create table if not exists faculty(faculty_id integer primary key,faculty_name text)')
db.commit();
# cursor.execute('insert into faculty VALUES (9,"dillep ad")');
# db.commit();
print('All table created')
master = Tk() 
master.title("Time table assist tool")
Label(master, text='Dummy').grid(row=0) 
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

Course_Dict = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4} 

def update_options(var, row_val):
	cr = cr_vars[var].get()
	if(old_var[var] == cr):
		return 0
	# print(row_val)
	if match[row_val][ord(cr)-65] == True:
		cr_vars[var].set("SLOT")
		messagebox.showerror("Error", "More than one occurance of a slot on same day")
		return 0
	match[row_val][ord(cr)-65] = True
	# print(match)
	Course_Dict[cr] -= 1
	if old_var[var] != "SLOT":
		Course_Dict[old_var[var]] += 1
		match[row_val][ord(old_var[var])-65] = False
	old_var[var] = cr
	if(Course_Dict[cr] < 0):
		cr_vars[var].set("SLOT")
		Course_Dict[cr] += 1
		messagebox.showerror("Error", "More than required slots")
	# print(Course_Dict[cr])

cr_vars = []
old_var = []
z = 0
match = [[False for i in range(8)] for j in range(6)]
# print(match)


for i in range(1,6):
    for j in range(1,10):
        cr_vars.append(StringVar(master))
        cr_vars[z].set("SLOT")
        old_var.append("SLOT")
        left_course = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        w = OptionMenu(master, cr_vars[z], *left_course)
        if(j != 5):
        	w.grid(row=i,column=j)
        cr_vars[z].trace("w", lambda *_, var=z, row_val=i: update_options(var, row_val))
        z = z + 1
mainloop() 
