import pytest
import requests
# @pytest.fixture()
# def data():
#     return 'hello'
#
# def test_data(data):
#     assert data=='hello'


# 利用fixture返回token或者seesion进行登录
#可以注释用#conftest.py 文件  共享fixtrue
# @pytest.fixture()
# def getToken():
#     '''获取token'''
#     r=requests.post(
#         url='http://127.0.0.1:5000/auth',
#         json={"username":"wuya","password":"asd888"}
#     )
#     return r.json()['access_token']

def test_get_allbook(getToken):
    r=requests.get(
        url='http://127.0.0.1:5000/v1/api/books',headers={'Authorization':'JWT {0}'.format(getToken)}
    )
    print(r.json())

if __name__ == '__main__':
    pytest.main(['-s','-v','test_oe.py'])