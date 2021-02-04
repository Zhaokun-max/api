import pytest
import requests
#执行的时候和其他一样，在当前目录下,如在上一级目录执行或者将bookID用os解决


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

# 获取书籍ID
def writebookid(bookID):
    with open('bookID', 'w') as f:
        f.write(str(bookID))

#可以定义为fix函数
#如果不使用的话，把init和del中的getbookid删除，在format里面调用函数
@pytest.fixture()
def getbookid():
    with open('bookID','r') as f:
        return f.read()


#添加书籍
def addbook(getToken):
    r=requests.post(
        url='http://127.0.0.1:5000/v1/api/books',
        json= {
            "author": "无涯",
            "done": False,
            "id": 2,
            "name": "Selenium3自动化测试实战"
        },
        headers={'Authorization':'JTW {0}'.format(getToken)}
    )
    writebookid(r.json()[0]['datas']['id'])
    print('添加书籍：\n', r.json())
#删除书籍
def delbook(getToken,getbookid):
    r=requests.delete(
        url='http://127.0.0.1:5000/v1/api/book/{0}'.format(getbookid),
        headers={'Authorization': 'JTW {0}'.format(getToken)})
    print('删除书籍：\n', r.json())

@pytest.fixture()
def init(getToken,getbookid):
    addbook(getToken)
    #yield 代表中间的部分
    yield
    delbook(getToken,getbookid)


def test_get_book(init,getToken,getbookid):
    r=requests.get(
        url='http://127.0.0.1:5000/v1/api/book/{0}'.format(getbookid),
        headers={'Authorization': 'JTW {0}'.format(getToken)}
    )

    print('查看书籍：\n',r.json())
