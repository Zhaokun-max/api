import unittest
import requests

class Requests:
    def request(self,url, method='get', **kwargs):
        if method=='get':
            return requests.request(url=url, method=method, **kwargs)
        elif method=='post':
            return requests.request(url=url, method=method, **kwargs)

        elif method=='delete':
            return requests.request(url=url, method=method, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url=url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method='post', **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url=url, method='delete', **kwargs)

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.obj=Requests()

    @property
    def getToken(self):
        data={'username':'wuya','password':'asd888'}
        r=self.obj.post(url='http://127.0.0.1:5000/auth', json=data)
        return r.json()['access_token']

    @property
    def getHeaders(self):
        headers={"Authorization": 'JWT {0}'.format(self.getToken),"Content-Type":"application/json"}
        return headers

    def write(self,bookID):
        with open('bookID',"w") as f:
            f.write(str(bookID))
    def read(self):
        with open('bookID','r') as f:
            return f.read()

    def addbook(self):
        '''添加书籍'''
        data = {"author": "无涯", "done": True, "name": "测试实战"}
        r = self.obj.post(url='http://127.0.0.1:5000/v1/api/books', json=data,
                          headers=self.getHeaders)
        return r

    def seletebook(self):
        '''查询'''
        r=self.obj.get(url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read()),
                       headers=self.getHeaders)
        return r

    def delbook(self):
        '''删除'''
        r = self.obj.delete(url='http://127.0.0.1:5000/v1/api/book/{0}'.format(self.read()),
                            headers=self.getHeaders)
        return r

    def test_book_c(self):
        '''添加书籍'''
        r = self.addbook()
        self.delbook()
        print(r.json())
        self.write(r.json()[0]['datas']['id'])
        self.assertEqual(r.json()[0]['status'],1002)
        self.assertEqual(r.status_code,200)

    def test_book_b(self):
        '''查询'''
        self.addbook()
        r= self.seletebook()
        self.delbook()
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['datas'][0]['name'],'测试实战')
        self.assertEqual(r.json()['status'],0)
        print(r.json())

    def test_book_a(self):
        '''删除'''
        self.addbook()
        r=self.delbook()
        self.assertEqual(r.json()['msg'],'删除书籍成功')
        self.assertEqual(r.json()['status'],1009)
        print(r.json())

    def test_book_004(self):
        '''查看'''
        r=self.obj.get(url='http://127.0.0.1:5000/v1/api/books',
                       headers=self.getHeaders)
        self.assertEqual(r.status_code,200)
        print(r.json())


if __name__ == '__main__':
    unittest.main(verbosity=2)