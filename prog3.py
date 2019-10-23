from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog


file_path = ""
lists=[]
master2 = Tk()
master2.title("SLot Selection")
master2.geometry("500x500+300+300")
frame1=Frame(master2,bd=10,height=500,padx=10,pady=10,width=1500)
v = StringVar(frame1)
frame1.pack()
slotA=[]
slotB=[]
slotC=[]
slotD=[]
slotE=[]
slotF=[]
slotG=[]
slotH=[]
frame2=Frame(master2,bd=10,height=500,padx=10,pady=10,width=1500)
frame2.pack()
def DisplayGUI():
    global file_path
    for widget in frame2.winfo_children():
        widget.destroy()
    
def DropDown():
    global lists,v,slotA,slotB,slotC,slotD,slotE,slotF,slotG
    v.set("Select Slot")
    for file in lists:
        a=str(os.path.join(file_path, file))
        wb = openpyxl.load_workbook(a)
        ws = wb.active
        for i in range(2,ws.max_row+1):
            if(ws.cell(i,5).value=="Slot A"):
                slotA.append(ws.cell(i,1).value)
            elif(ws.cell(i,5).value=="Slot B"):
                slotB.append(ws.cell(i,1).value)
            elif(ws.cell(i,5).value=="Slot C"):
                slotC.append(ws.cell(i,1).value)
            elif(ws.cell(i,5).value=="Slot D"):
                slotD.append(ws.cell(i,1).value)
            elif(ws.cell(i,5).value=="Slot E"):
                slotE.append(ws.cell(i,1).value)
            elif(ws.cell(i,5).value=="Slot F"):
                slotF.append(ws.cell(i,1).value)
            elif(ws.cell(i,5).value=="Slot G"):
                slotG.append(ws.cell(i,1).value)
            else:
                slotH.append(ws.cell(i,1).value)    


    slots=['Slot A','Slot B','Slot C','Slot D','Slot E','Slot F','Slot G','Slot H']
    w = OptionMenu(frame1, v, *slots)
    w.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
    w.config(width=45)
    v.trace("w", DisplayGUI)

def DialogBox():
       global file_path
       file_path=filedialog.askdirectory()
       for file in os.listdir(file_path):
           if file.endswith('.xlsx') and file!="track.xlsx":
               a=str(os.path.join(file_path, file))
               lists.append(file)
       DropDown()

B = Button(frame1, text ="Choose Directory", command = DialogBox)
B.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)
B.config(width=45)

mainloop()