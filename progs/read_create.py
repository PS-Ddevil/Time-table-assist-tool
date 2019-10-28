import pandas as pd
import ezodf
import os
import xlsxwriter
import openpyxl

file_name = "../src/data/CourselistAug-Dec2019_2Sep.ods"

doc = ezodf.opendoc(file_name)
sheet = doc.sheets[0]
df_dict = {}
i=0
new_dict = {}
for i,row in enumerate(sheet.rows()):
    df_dict = {cell.value:[] for cell in row}
    col_index = {j:cell.value for j, cell in enumerate(row)}
    p=0
    
    for p in range(50):
        if(col_index[p]=='C'):
            wb = openpyxl.Workbook()
            wb.save(str(p) + ".xlsx")
            # print(df_dict)
            book = xlsxwriter.Workbook(str(p) + ".xlsx")
            sheet = book.add_worksheet()
            ws = wb.worksheets[0]
            headers = df_dict.keys()
            k=0
            rows = ws.max_row
            # print("file name ----",str(p),"   ",rows)
            for(idx,header) in enumerate(headers):
                # print("----------",idx,header,"-----------")
                sheet.write(rows,idx,header)
                # print(headers)
            book.close()
            break







        






