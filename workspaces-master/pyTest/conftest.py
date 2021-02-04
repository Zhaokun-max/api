import pytest
import requests

@pytest.fixture()
def getToken():
    '''获取token'''
    r=requests.post(
        url='http://127.0.0.1:5000/auth',
        json={"username":"wuya","password":"asd888"}
    )
    return r.json()['access_token']






#关联inFixture里面test_one 函数
def pytest_addoption(parser):
    #defa 默认命令行--foo  默认输出admin help 帮助文档
    #多个默认命令行 pytest -s -v test_oe.py::test_login_auth --username=admin --password=admin

    parser.addoption('--foo', action='store', default='admin', help='')
    parser.addoption('--username', action='store', default='wuya', help='')
    parser.addoption('--password', action='store', default='asd888', help='')

@pytest.fixture()
def getfoo(request):
    return request.config.getoption('--foo')

@pytest.fixture()
def username(request):
    return request.config.getoption('--username')

#返回值函数
@pytest.fixture()
def password(request):
    return request.config.getoption('--password')