from base.method import Requests
from utils.operationYaml import OperationYaml
from utils.operationExcel import OperationExcel
import requests
import pytest
import json

class TestBook():
    excel=OperationExcel()
    obj=Requests()

    def result(self,r,row):
        assert r.status_code == 200
        assert self.excel.get_Expect(row=row) in json.dumps(r.json(),ensure_ascii=False)


    def test_book_001(self):
        '''获取所书籍信息'''
        r= self.obj.get(url=self.excel.getUrl(row=1))
        #asciiFalse或者True都可以，可以把json封装成方法
        #assert self.excel.get_Expect(row=1) in json.dumps(r.json(),ensure_ascii=False)
        self.result(row=1,r=r)

    def test_book_002(self):
        '''添加书籍'''
        r=self.obj.post(url=self.excel.getUrl(row=2),
                        json=self.excel.getJson(row=2))
        print(r.json())

if __name__ == '__main__':
    pytest.main(['-s','-v','test_book.py::TestBook::test_book_002'])