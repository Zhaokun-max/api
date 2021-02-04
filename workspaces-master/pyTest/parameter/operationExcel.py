import xlrd

def readExcel():
    data=list()
    boox=xlrd.open_workbook('login.xls')
    sheet=book.sheet_by_index(0)
    for item in range(1,sheet.nrows):
        print(sheet.row_values(item))
    return data
readExcel()