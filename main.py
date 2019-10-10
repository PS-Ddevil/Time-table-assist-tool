from tkinter import *
master = Tk() 
master.title("Time table assist tool")
Label(master, text='Dummy').grid(row=0) 
Label(master, text='8:00 - 8:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=1) 
Label(master, text='9:00 - 9:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=2) 
Label(master, text='10:00 - 10:50',borderwidth=2, relief="solid",bg='yellow').grid(row=0,column=3) 
Label(master, text='11:00 - 11:50',borderwidth=2, relief="solid",bg='orange').grid(row=0,column=4) 
Label(master, text='LUNCH BREAK',borderwidth=2, relief="solid").grid(row=0,column=5)
Label(master, text='1:00 - 1:50',borderwidth=2, relief="solid",bg='blue').grid(row=0,column=6) 
Label(master, text='2:00 - 2:50',borderwidth=2, relief="solid",bg='pink').grid(row=0,column=7) 
Label(master, text='3:00 - 3:50',borderwidth=2, relief="solid",bg='green').grid(row=0,column=8) 
Label(master, text='4:00 - 4:50',borderwidth=2, relief="solid",bg='red').grid(row=0,column=9) 
# Label(master, text='nenfekw').grid(row=0,column=9) 
# Label(master, text='nenfekw').grid(row=0,column=10) 
# Label(master, text='nenfekw').grid(row=0,column=13) 

Label(master, text='Monday',borderwidth=2, relief="solid",bg='red').grid(row=1) 
Label(master, text='Tuesday',borderwidth=2, relief="solid",bg='blue').grid(row=2) 
Label(master, text='Wednesday',borderwidth=2, relief="solid",bg='green').grid(row=3) 
Label(master, text='Thrusday',borderwidth=2, relief="solid",bg='yellow').grid(row=4) 
Label(master, text='Friday',borderwidth=2, relief="solid",bg='pink').grid(row=5) 
variable = StringVar(master)
variable.set("Course") # default value

for i in range(1,6):
    for j in range(1,10):
        # print (i,j)
        w = OptionMenu(master, variable ,"one", "two", "three")
        w.grid(row=i,column=j)
mainloop() 
