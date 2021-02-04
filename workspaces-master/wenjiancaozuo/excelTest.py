
import xlrd
import os
from xlutils.copy import copy
#读取目录
def base_dir(filename=None):
    #当前目录下
    #return os.path.dirname(__file__)
    return os.path.join(os.path.dirname(__file__),filename)
'''文件的操作'''
'''
#读取打开文件
work=xlrd.open_workbook(base_dir('data.xls'))
#具体到行或者seheet
#按照索引读取，sheet1，sheet2  按照索引读取定位sheet
#按照name就写入名字 sheet1
sheet=work.sheet_by_index(0)
#查看多少行
print(sheet.nrows)
#获取单元格的内容,行为10，列为1
print(sheet.cell_value(10,1))
'''

'''excel文件内容的修改'''
#首先读取excel找到它的对象
work=xlrd.open_workbook(base_dir('data.xls'))
#把之前的文件内容保存下来,复制
old_content=copy(work)
#对哪个excel文件进行操作,索引为0，是第一个sheet
ws=old_content.get_sheet(0)
ws.write(9,2,'盼达')
#把之前的内容重新写到新的excel，然后修改，写入之后保存另一个文件
old_content.save(base_dir('excel1.xls'))