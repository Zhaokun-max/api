

import pytest
import requests

@pytest.fixture()
def login():
    r=requests.post(
        url='http://127.0.0.1:5000/auth',
        json={"username":'wuya',"password":'asd888'}
    )
    return r.json()['access_token']

def test_get_books(tmpdir,login):
    #创建操作文件的对象。创建临时文件token
    f=tmpdir.join('token.txt')
    #io写操作内容，把token写入临时文件当中
    f.write(login)
    r=requests.get(url='http://127.0.0.1:5000/v1/api/books',
                   headers={'Authorization':'JWT {0}'.format(f.read())})
    print('\n结果信息:',r.json())

if __name__ == '__main__':
    pytest.main(['-s','-v','test_tmdir_actual.py'])