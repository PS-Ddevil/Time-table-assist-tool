from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
import sqlite3

def TimeTable():
	db=sqlite3.connect('Time table')
	cursor=db.cursor()
	cursor.execute('create table if not exists subject(subject_code text primary key,subject_name text,slot_id text,FOREIGN KEY(slot_id) REFERENCES slot(slot_id))')
	db.commit()
	cursor.execute('create table if not exists slot(slot_id text primary key,faculty_id integer,FOREIGN KEY(faculty_id) REFERENCES faculty(facluty_id) )')
	db.commit()
	cursor.execute('create table if not exists faculty(faculty_id integer primary key,faculty_name text)')
	db.commit()
	print('All table created')
	master = Tk() 
	master.title("Time table assist tool")

	# DEFINING THE GUI ELEMENTS
	Label(master,width=20,height=2, text='').grid(row=0) 
	Label(master,width=20,height=2, text='8:00 - 8:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=1) 
	Label(master,width=20,height=2, text='9:00 - 9:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=2) 
	Label(master,width=20,height=2, text='10:00 - 10:50',borderwidth=2, relief="solid",bg='yellow').grid(row=0,column=3) 
	Label(master,width=20,height=2, text='11:00 - 11:50',borderwidth=2, relief="solid",bg='orange').grid(row=0,column=4) 
	Label(master,width=20, text='LUNCH BREAK',borderwidth=2, relief="solid").grid(row=0,column=5, rowspan=5)
	Label(master,width=20,height=2, text='1:00 - 1:50',borderwidth=2, relief="solid",bg='blue').grid(row=0,column=6) 
	Label(master,width=20,height=2, text='2:00 - 2:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=7) 
	Label(master,width=20,height=2, text='3:00 - 3:50',borderwidth=2, relief="solid",bg='green').grid(row=0,column=8) 
	Label(master,width=20,height=2, text='4:00 - 4:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=9) 
	Label(master,width=20,height=2, text='Monday',borderwidth=2, relief="solid",bg='red').grid(row=1) 
	Label(master,width=20,height=2, text='Tuesday',borderwidth=2, relief="solid",bg='blue').grid(row=2) 
	Label(master,width=20,height=2, text='Wednesday',borderwidth=2, relief="solid",bg='green').grid(row=3) 
	Label(master,width=20,height=2, text='Thrusday',borderwidth=2, relief="solid",bg='yellow').grid(row=4) 
	Label(master,width=20,height=2, text='Friday',borderwidth=2, relief="solid",bg='pink').grid(row=5) 

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



file_path = ""
def Basket():
	
	master2 = Tk()
	master2.title("SLot Selection")
	master2.geometry("500x500+300+300")
	frame1=Frame(master2,bd=10,height=500,padx=10,pady=10,width=1500)
	frame1.pack()
	v = StringVar(frame1)
	lists=[]
	vars = []

	def DropDown():

		print("  678")	
		v.set("Select File")
		w = OptionMenu(frame1, v, *lists)
		w.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
		w.config(width=45)
		v.trace("w", DisplayGUI)
		print("  678")

	def ConstraintCheck(var,i,name,focus,*args):
		print("  123  ")
		global file_path
		wb = openpyxl.load_workbook(str(os.path.join(file_path, v.get())))
		ws = wb.active
		j=0
		for j in range(2,ws.max_row+1):
			c1=ws.cell(j,5)
			if i==j:
				continue
			if c1.value==var.get():
				messagebox.showerror("Error", var.get() + " is twice time and it will not be saved so please change ") 
				var.set(ws.cell(i,5).value)
				#print(var.get())
				break
		wb.save(str(os.path.join(file_path, v.get())))
		prof=ws.cell(i,4).value
		for file in lists:
			if(file==v.get()):
				continue
			wb = openpyxl.load_workbook(str(os.path.join(file_path, file)))
			ws=wb.active
			for k in range(2,ws.max_row+1):
				if ws.cell(k,4).value==prof and ws.cell(k,5).value==var.get():
					
					messagebox.showerror("Error", prof + " has same slot in "+ file)
					wb.save(file)
					var.set(ws.cell(i,5).value)
					return
			wb.save(file)
		
		wb = openpyxl.load_workbook(str(os.path.join(file_path, v.get())))
		ws = wb.active
		if j==ws.max_row :
			c1=ws.cell(i,5)
			c1.value=var.get()
		
			
		wb.save(str(os.path.join(file_path, v.get())))
		print("  123   ")

	frame2=Frame(master2,bd=10,height=500,padx=10,pady=10,width=1500)
	frame2.pack()
	def DisplayGUI(*args):
		print("  345")
		global file_path
		for widget in frame2.winfo_children():
			widget.destroy()
		print(file_path,"  ",v.get())
		wb = openpyxl.load_workbook(str(os.path.join(file_path, v.get())))
		ws = wb.active
		slots=['Slot A','Slot B','Slot C','Slot D','Slot E','Slot F','Slot G','Slot H']
		c1=ws.cell(1,5)
		if c1.value is None: 
			c1.value="Slots"
		w = Label(frame2, text="Course")
		w.grid(row=2,column=0,columnspan=1,sticky=W+E+N+S)
		w = Label(frame2, text="Prof")
		w.grid(row=2,column=1,columnspan=1,sticky=W+E+N+S)
		w = Label(frame2, text="Slots")
		w.grid(row=2,column=2,columnspan=1,sticky=W+E+N+S)
		for i in range(2,ws.max_row+1):
			c1=ws.cell(i,5)
			var = StringVar(frame2)
			if c1.value is None: 
				c1.value="No Slots"
				var.set("No Slots")
			else:
				var.set(c1.value)
			vars.append(var)
			w = Label(frame2, text=ws.cell(i,1).value)
			w.grid(row=i+2,column=0,columnspan=1,sticky=W+E+N+S)
			w.config(width=15)
			w = Label(frame2, text=ws.cell(i,4).value)
			w.grid(row=i+2,column=1,columnspan=1,sticky=W+E+N+S)
			w.config(width=15)
			w = OptionMenu(frame2,var,*slots)
			w.grid(row=i+2,column=2,sticky=W+E+N+S)
			w.config(width=15)
			var.trace("w", lambda name1,name2,op,i=i,var=var,name=v.get(),focus=w:ConstraintCheck(var,i,name,focus,name1,name2,op))
		wb.save(str(os.path.join(file_path, v.get())))
		print("   345")

	def DialogBox():
		print(" 234 ")
		global file_path
		file_path=filedialog.askdirectory()
		
		a=str(os.path.join(file_path, "track.xlsx"))
		wb = openpyxl.load_workbook(a)
		ws = wb.active
		course=[]
		faculty=[]
		for i in range(2,ws.max_row+1):
				course.append(ws.cell(i,1).value)
				faculty.append(ws.cell(i,2).value)
		wb.save(a)
		for file in os.listdir(file_path):
			if file.endswith('.xlsx') and file!="track.xlsx":
				a=str(os.path.join(file_path, file))
				lists.append(file)
				wb = openpyxl.load_workbook(a)
				ws = wb.active
				if ws.cell(3,4).value is None :
						ws.cell(1,4).value="Faculty"
						for i in range(2,ws.max_row+1):
							c1=ws.cell(i,1).value
							for j in range(len(course)):
								if c1==course[j]:
									ws.cell(i,4).value=faculty[j]
									break
				wb.save(a)
		DropDown()
		print("  234 ")
	B = Button(frame1, text ="Choose Directory", command = DialogBox)
	B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
	B.config(width=45)




master = Tk()
master.title("Time Table Assist Tool")
<<<<<<< HEAD
frame=Frame(master,bd=10,height=500,padx=10,pady=10,width=1500)
frame.pack()
B = Button(frame, text ="Time Table", command = TimeTable)
B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
B = Button(frame, text ="BaSket", command = Basket)
B.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)
mainloop()
=======

mainloop()
>>>>>>> upstream/master
