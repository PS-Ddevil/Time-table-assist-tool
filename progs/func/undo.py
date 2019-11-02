import xlrd
def undo_in_excel_sheet(cr_vars):
    # Give the location of the file
    filename = ("../src/data/slot.xlsx")
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    count=0
    for i in range(1,6):
        for j in  range(1,10):
            if(j!=5):
                cr_vars[count].set(sheet.cell_value(i,j))
            count=count+1
