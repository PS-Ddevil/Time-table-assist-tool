from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
import tkinter.ttk as ttk


lists=[]
matrix = [[] for _ in range(11)]
file_path = "/home/vinay/Documents/Learn/Time-table-assist-tool/src/tmp/baskets"

def final_time_table():
    for file in os.listdir(file_path):
        lists.append(file)
        # print(file)
        a=str(os.path.join(file_path, file))
        wb = openpyxl.load_workbook(a)
        ws = wb.active
        # print(a)
        for i in range(1,ws.max_row+1):
            # print(ws.cell(i,8).value)
            if(str(ws.cell(i,8).value) == "Slot A"):
                matrix[0].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot B"):
                matrix[1].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot C"):
                matrix[2].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot D"):
                matrix[3].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot E"):
                matrix[4].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot F"):
                matrix[5].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot G"):
                matrix[6].append(str(ws.cell(i,1).value))
            elif(str(ws.cell(i,8).value) == "Slot H"):
                matrix[7].append(str(ws.cell(i,1).value))
    
    # wb = openpyxl.Workbook()
    # wb.save("resultant matrix" + ".xlsx")
    # wb = openpyxl.load_workbook("resultant matrix" + ".xlsx")
    # ws = wb.worksheets[0]
    for i in range(1,10):
        matrix[i]=list(dict.fromkeys(matrix[i]))
        print("----------------")
        print(matrix[i])
        print("----------------")


    # for i in range(1,10):
    #     for j in range(1,len(matrix[i])):
    #         ws.cell(i,j).value = matrix[i][j]
    #         wb.save("resultant matrix" + ".xlsx")
    
    # wb.save("resultant matrix" + ".xlsx")




    


final_time_table()   