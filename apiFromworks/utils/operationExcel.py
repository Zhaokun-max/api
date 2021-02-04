import xlrd
from common.pubilc import filePath
from utils.operationYaml import OperationYaml

class ExcelValue():
    #分装excel
    #分别对应book第一行表的ID等
    caseID=0
    des=1
    url=2
    met=3
    data=4
    expect=5

    @property
    def getCaseID(self):
        return self.caseID

    @property
    def getDescription(self):
        return self.des

    @property
    def geturl(self):
        return self.url

    @property
    def getmethod(self):
        return self.met

    @property
    def getData(self):
        return self.data

    @property
    def getExpect(self):
        return self.expect

class OperationExcel(OperationYaml):
    def getSheet(self):
        book=xlrd.open_workbook(filePath('data','book.xlsx'))
        return book.sheet_by_index(0)
    @property
    def getRow(self):
        '''
        获取总行数
        :return:
        '''
        return self.getSheet().nrows
    @property
    def getCols(self):
        '''
        获取总列数
        :return:
        '''
        return self.getSheet().ncols

    def getValues(self,row,col):
        #获取多少行的多少列，调用传参数row，col
        return self.getSheet().cell_value(row,col)

    def getCaseID(self,row):
        #获取ID
        return self.getValues(row=row,col=ExcelValue().getCaseID)

    def getUrl(self,row):
        #获取url
        return self.getValues(row=row,col=ExcelValue().geturl)

    def getMethod(self,row):
        #获取请求方法
        return self.getValues(row=row,col=ExcelValue().getmethod)

    def getData(self, row):
        #获取caseID
        return self.getValues(row=row, col=ExcelValue().getData)

    def getJson(self,row):
        #获取请求数据
        return self.dictYaml()[self.getData(row=row)]
        #return self.getValues(row=row,col=ExcelValue().getData)

    def get_Expect(self,row):
        #获取期望结果
        return self.getValues(row=row,col=ExcelValue().getExpect)



# if __name__ == '__main__':
#     obj=OperationExcel()
#     #print(obj.getData(2))
#     print(obj.getJson(2))
#     print(type(obj.getJson(2 )))
#     # print(obj.getCaseID(row=4))
#     # print(obj.getUrl(row=4))
#     # print(obj.getMethod(row=4))
#     # print(obj.get_Data(row=4))
