import requests
import json
import unittest
import warnings
from test_partal_data.ProjectData import *
from test_partal_data.getHeaders import Get_headers
from test_partal_data.getUrl import GetUrl
from test_partal_data.method import Requests
import time
import pytest
headers = Get_headers()
url = GetUrl()

json = Publish_Data()
class Test_House():
    '''房屋建筑'''
    obj = Requests()
    warnings.simplefilter('ignore', ResourceWarning)
    def get(self, ID):
        with open('ID', "w") as f:
            f.write(str(ID))

    @property

    def read(self):
        '''获取id'''
        with open('ID', 'r') as f:
            return f.read()

    def test_publish_001(self):
        '''发布编辑项目信息'''
        r = self.obj.post(url=url.getUrl_001, json=json.building_001, headers=headers.getheaders)
        print(r.json())
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code'] == str(0)
        else:
            self.get(r.json()['data'])

    def test_publish_002(self):
        '''发布编辑受让信息'''
        r = self.obj.post(url=url.getUrl_002, json=json.building_002, headers=headers.getheaders)
        assert r.json()['code'] == str(0)
        assert r.json()['data'] == int(self.read)

    def test_publish_003(self):
        '''上传图片'''
        for i in range(10):
            r = self.obj.post(url=url.getUrl_003, files=json.building_file, headers=headers.getheaders_002,
                              json=json.building_003)
            if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
                assert r.json()['code'] == str(0)
            else:
                self.save_photo(r.json()['data']['fullPath'])

    def save_photo(self, photo):
        '''保存图片地址'''
        with open('photo', 'a') as f:
            f.write(str(photo) + '\n')

    def test_publish_004(self):
        '''发布上传附件信息'''
        r = self.obj.post(url=url.getUrl_004, json=json_clf.building_004, headers=headers.getheaders)
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code'] == str(0)

    def test_publish_005(self):
        '''确认承诺函'''
        r = self.obj.post(url=url.getUrl_005, json=json.building_005, headers=headers.getheaders)
        assert r.json()['code'] == str(0)

    def test_publish_006(self):
        '''清空photo'''
        with open('photo', 'r+', encoding='utf-8', ) as f:
            f.truncate(0)

json_Cml= Publish_Cml()
class Test_Cml():
    '''集体机动地'''
    obj = Requests()
    warnings.simplefilter('ignore', ResourceWarning)

    def get(self,ID):
        with open('ID', "w") as f:
            f.write(str(ID))

    @property
    def read(self):
        '''获取id'''
        with open('ID', 'r') as f:
            return f.read()

    def test_Cml_001(self):
        '''发布编辑项目信息'''
        r=self.obj.post(url=url.getUrl_001, json=json_Cml.building_001, headers=headers.getheaders)
        print(r.json())
        if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
            assert r.json()['code'] == str(0)
        else:
            self.get(r.json()['data'])

    def test_Cml_002(self):
        '''发布编辑受让信息'''
        r = self.obj.post(url=url.getUrl_002, json=json_Cml.building_002, headers=headers.getheaders)
        assert r.json()['code'] == str(0)
        assert r.json()['data'] == int(self.read)

    def test_Cml_003(self):
        '''上传图片'''
        for i in range(10):
            r = self.obj.post(url=url.getUrl_003, files=json_Cml.building_file, headers=headers.getheaders_002,json=json.building_003)
            if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
                assert r.json()['code'] == str(0)
            else:
                self.save_photo(r.json()['data']['fullPath'])
            #time.sleep(2)

    def save_photo(self,photo):
        '''保存图片地址'''
        with open('photo', 'a') as f:
            f.write(str(photo)+'\n')

    def test_Cml_004(self):
        '''发布上传附件信息'''
        r = self.obj.post(url=url.getUrl_004,data=json_clf.building_004,headers=headers.getheaders)
        #print(json_Cml.building_004)
        #print(type(json_Cml.building_004))
        print(r.json())
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code'] == str(0)

    def test_Cml_005(self):
        '''确认承诺函'''
        r=self.obj.post(url=url.getUrl_005,json=json_Cml.building_005,headers=headers.getheaders)
        assert r.json()['code'] == str(0)

    # def test_Cml_006(self):
    #     '''清空photo'''
    #     with open('photo', 'r+', encoding='utf-8', ) as f:
    #         f.truncate(0)

json_clf = Publish_Clf()
class Test_Clf():
    '''农户承包地'''
    obj = Requests()
    warnings.simplefilter('ignore', ResourceWarning)

    def get(self,ID):
        with open('ID', "w") as f:
            f.write(str(ID))

    @property
    def read(self):
        '''获取id'''
        with open('ID', 'r') as f:
            return f.read()

    def test_clf_001(self):
        '''发布编辑项目信息'''
        r=self.obj.post(url=url.getUrl_001, json=json_clf.clf_001, headers=headers.getheaders)
        if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
            assert r.json()['code'] == str(0)
        else:
            self.get(r.json()['data'])

    def test_clf_002(self):
        '''发布编辑受让信息'''
        r = self.obj.post(url=url.getUrl_002, json=json_clf.clf_002, headers=headers.getheaders)
        assert r.json()['code'] == str(0)
        assert r.json()['data'] == int(self.read)

    def test_clf_003(self):
        '''上传图片'''
        for i in range(10):
            r = self.obj.post(url=url.getUrl_003, files=json_clf.building_file, headers=headers.getheaders_002,json=json_clf.clf_003)
            if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
                assert r.json()['code'] == str(0)
            else:
                self.save_photo(r.json()['data']['fullPath'])

    def save_photo(self,photo):
        '''保存图片地址'''
        with open('photo', 'a') as f:
            f.write(str(photo)+'\n')

    def test_clf_004(self):
        '''发布上传附件信息'''
        r = self.obj.post(url=url.getUrl_004,json=json_clf.clf_004,headers=headers.getheaders)
        print(r.json())
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code'] == str(0)

    def test_clf_005(self):
        '''确认承诺函'''
        r=self.obj.post(url=url.getUrl_005,json=json_clf.clf_005,headers=headers.getheaders)
        assert r.json()['code'] == str(0)
    def test_clf_006(self):
        '''清空photo'''
        with open('photo', 'r+', encoding='utf-8', ) as f:
            f.truncate(0)

json_wd = Publish_Woodland()
class Test_Wd():
    '''林地'''
    obj = Requests()
    warnings.simplefilter('ignore', ResourceWarning)

    def get(self,ID):
        with open('ID', "w") as f:
            f.write(str(ID))

    @property
    def read(self):
        '''获取id'''
        with open('ID', 'r') as f:
            return f.read()

    def test_wd_001(self):
        '''发布编辑项目信息'''
        r=self.obj.post(url=url.getUrl_001, json=json_wd.building_001, headers=headers.getheaders)
        print(r.json())
        if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
            assert r.json()['code'] == str(0)
        else:
            self.get(r.json()['data'])

    def test_wd_002(self):
        '''发布编辑受让信息'''
        r = self.obj.post(url=url.getUrl_002, json=json_wd.building_002, headers=headers.getheaders)
        assert r.json()['code'] == str(0)
        assert r.json()['data'] == int(self.read)

    def test_wd_003(self):
        '''上传图片'''
        for i in range(10):
            r = self.obj.post(url=url.getUrl_003, files=json_wd.building_file, headers=headers.getheaders_002,json=json.building_003)
            print(r.json())
            if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
                assert r.json()['code'] == str(0)
            else:
                self.save_photo(r.json()['data']['fullPath'])

    def save_photo(self,photo):
        '''保存图片地址'''
        with open('photo', 'a') as f:
            f.write(str(photo)+'\n')

    def test_wd_004(self):
        '''发布上传附件信息'''
        r = self.obj.post(url=url.getUrl_004,json=json_clf.building_004,headers=headers.getheaders)
        print(r.json())
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code'] == str(0)

    def test_wd_005(self):
        '''确认承诺函'''
        r=self.obj.post(url=url.getUrl_005,json=json_wd.building_005,headers=headers.getheaders)
        assert r.json()['code'] == str(0)

    def test_publish_006(self):
        '''清空photo'''
        with open('photo', 'r+', encoding='utf-8', ) as f:
            f.truncate(0)

json_wr= Publish_water()
class Test_Wr():
    '''水面'''
    obj = Requests()
    warnings.simplefilter('ignore', ResourceWarning)
    def get(self,ID):
        with open('ID', "w") as f:
            f.write(str(ID))

    @property
    def read(self):
        '''获取id'''
        with open('ID', 'r') as f:
            return f.read()

    def test_wr_001(self):
        '''发布编辑项目信息'''
        r=self.obj.post(url=url.getUrl_001, json=json_wr.building_001, headers=headers.getheaders)
        print(r.json())
        if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
            assert r.json()['code'] == str(0)
        else:
            self.get(r.json()['data'])

    def test_wr_002(self):
        '''发布编辑受让信息'''
        r = self.obj.post(url=url.getUrl_002, json=json_wr.building_002, headers=headers.getheaders)
        assert r.json()['code'] == str(0)
        assert r.json()['data'] == int(self.read)

    def test_wr_003(self):
        '''上传图片'''
        for i in range(10):
            r = self.obj.post(url=url.getUrl_003, files=json_wr.building_file, headers=headers.getheaders_002,json=json.building_003)
            if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
                assert r.json()['code'] == str(0)
            else:
                self.save_photo(r.json()['data']['fullPath'])

    def save_photo(self,photo):
        '''保存图片地址'''
        with open('photo', 'a') as f:
            f.write(str(photo)+'\n')

    def test_wr_004(self):
        '''发布上传附件信息'''
        r = self.obj.post(url=url.getUrl_004,json=json_clf.building_004,headers=headers.getheaders)
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code'] == str(0)

    def test_wr_005(self):
        '''确认承诺函'''
        r=self.obj.post(url=url.getUrl_005,json=json_wr.building_005,headers=headers.getheaders)
        assert r.json()['code'] == str(0)

    def test_wr_006(self):
        '''清空photo'''
        with open('photo', 'r+', encoding='utf-8', ) as f:
            f.truncate(0)

json_Em= Publish_Equipment()
class Test_Em():
    '''设备'''
    obj = Requests()
    warnings.simplefilter('ignore', ResourceWarning)

    def get(self,ID):
        with open('ID', "w") as f:
            f.write(str(ID))

    @property
    def read(self):
        '''获取id'''
        with open('ID', 'r') as f:
            return f.read()

    def test_Em_001(self):
        '''发布编辑项目信息'''
        r=self.obj.post(url=url.getUrl_001, json=json_Em.building_001, headers=headers.getheaders)
        print(r.json())
        if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
            assert r.json()['code'] == str(0)
        else:
            self.get(r.json()['data'])

    def test_Em_002(self):
        '''发布编辑受让信息'''
        r = self.obj.post(url=url.getUrl_002, json=json_Em.building_002, headers=headers.getheaders)
        assert r.json()['code']==str(0)
        assert r.json()['data'] == int(self.read)
        #assert self.excel.get_Expect(row=row) in json.dumps(r.json(), ensure_ascii=False)

    def test_Em_003(self):
        '''上传图片'''
        for i in range(10):
            r = self.obj.post(url=url.getUrl_003, files=json_Em.building_file, headers=headers.getheaders_002,json=json.building_003)
            if r.json()['code']==None or r.json()['data']==None or r.json()['data']==999:
                assert r.json()['code']==str(0)
            else:
                self.save_photo(r.json()['data']['fullPath'])

    def save_photo(self,photo):
        '''保存图片地址'''
        with open('photo', 'a') as f:
            f.write(str(photo)+'\n')

    def test_Em_004(self):
        '''发布上传附件信息'''
        r = self.obj.post(url=url.getUrl_004,json=json_clf.building_004,headers=headers.getheaders)
        if r.json()['code'] == None or r.json()['data'] == None or r.json()['data'] == 999:
            assert r.json()['code']==str(0)

    def test_Em_005(self):
        '''确认承诺函'''
        r=self.obj.post(url=url.getUrl_005,json=json_Em.building_005,headers=headers.getheaders)
        assert r.json()['code']==str(0)

    def test_Em_006(self):
        '''清空photo'''
        with open('photo', 'r+', encoding='utf-8', ) as f:
            f.truncate(0)

if __name__ == '__main__':
    while True:
        try:
            i = int(input('请输入需要创建的项目类型：\n 1.房屋建筑物 2.集体机动地\n 3.农户承包地 4.林地林木\n 5.水面 6.设备设施\n 7.退出\n'))
            if i == 1:
                pytest.main(['-s', '-v', 'test_portal_api.py::Test_House'])
                break
            elif i == 2:
                pytest.main(['-s', '-v', 'test_portal_api.py::Test_Cml'])
                break
            elif i == 3:
                pytest.main(['-s', '-v', 'test_portal_api.py::Test_Clf'])
                break
            elif i == 4:
                pytest.main(['-s', '-v', 'test_portal_api.py::Test_Wd'])
                break
            elif i == 5:
                pytest.main(['-s', '-v', 'test_portal_api.py::Test_Wr'])
                break
            elif i == 6:
                pytest.main(['-s', '-v', 'test_portal_api.py::Test_Em'])
                break
            elif i == 7:
                break
            else:
                print('输入正确的数字')
        except Exception as f:
            print('执行失败,请检查输入的内容and执行命令')





