from tkinter import *
from tkinter import messagebox
import os
import openpyxl
from tkinter import filedialog
import tkinter.ttk as ttk


lists=[]
matrix = [[] for _ in range(11)]
mat = [[] for _ in range(30)]
file_path = "./src/tmp/baskets"

def final_time_table():
    for j in range(8):
        matrix[j].append(str(chr(ord('A')+j)))
        # print(matrix[j])
    for file in os.listdir(file_path):
        if file.endswith(".xlsx") and file != ".xlsx" and file!="course_faculty_main.xlsx" and file!='course_faculty_optional.xlsx':

            lists.append(file)
            # print(file)
            a=str(os.path.join(file_path, file))
            wb = openpyxl.load_workbook(a)
            ws = wb.active
            # print(a)
            for i in range(1,ws.max_row+1):
                # print(ws.cell(i,8).value)
                if(str(ws.cell(i,8).value) == "Slot A"):
                    matrix[0].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot B"):
                    matrix[1].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot C"):
                    matrix[2].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot D"):
                    matrix[3].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot E"):
                    matrix[4].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot F"):
                    matrix[5].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot G"):
                    matrix[6].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
                elif(str(ws.cell(i,8).value) == "Slot H"):
                    matrix[7].append(str(ws.cell(i,1).value) +" - (" + str(ws.cell(i,9).value) + ")")
    


    wb = openpyxl.Workbook()
    wb.save("Courses-Slot-wise" + ".xlsx")
    wb = openpyxl.load_workbook("Courses-Slot-wise" + ".xlsx")
    ws = wb.worksheets[0]
    for i in range(0,10):
        matrix[i]=list(dict.fromkeys(matrix[i]))
    
    for i in range(10):
        for j in range(0,len(matrix[i])):
            mat[j].append(matrix[i][j])
    #     print("----------------")
    #     print(matrix[i])
    #     print("----------------")
    print(mat)

    for i in range(0,10):
        for j in range(0,len(mat[i])):
            ws.cell(i+1,j+1).value = mat[i][j]
            wb.save("Courses-Slot-wise" + ".xlsx")
    
    wb.save("Courses-Slot-wise" + ".xlsx")




    


final_time_table()   