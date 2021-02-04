'''
1.发送请求登录
2.登录成功后，服务端返回客户端的响应数据中，包含了toke
3.每次登录token都不一样，token是令牌的作用
4.客户端再次发送请求（比如查看个人主页），那么就U型要在客户端里面带上token
   a.客户端的请求参数里面{"user":"3465","token":"sadasd32"}
   b.请求头里面
5.把token发送给服务端，服务端拿到token和存储在服务器端的token进行对比，如果一致那么通过
如果对比不一致，重定向登录页面
'''
import requests
# r=requests.get(url='http://127.0.0.1:5000/v1/api/books')
#没有token会提示没有token，重定向登录
# print(r.text)

def login():
    data={"username":"wuya","password":"asd888"}
    r=requests.post(url='http://127.0.0.1:5000/auth',
                   json=data)
    return r.json()["access_token"]

def books():
    headers={"Authorization":"JWT {0}".format(login())}
    r=requests.get(url='http://127.0.0.1:5000/v1/api/books',
                   headers=headers)
    print(r.text)
if __name__ == '__main__':
    books()