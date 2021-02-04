


import requests
def test_login():
    deic={
        "password":"123456",
        "username":"1881111222"
    }
    r=requests.post(url='http://test.admin.jlncjy.cacfintech.com/api/v1.0/chanquan/user/login',
                    json=deic)
    #print(r.json())
    #in  判断一个值是否包含另外一个值里面  对应的是字符串的类型
    assert '用户不存在，请重新输入。' in r.json()['reason']