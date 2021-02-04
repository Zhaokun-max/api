

'''
1.发送登录请求
2.登录成功后，把sessionID的信息返回客户端
3.客户端再次发送请求，需要在请求头里面(cookie)带上返回的sessionID
4.客户端带着ID发送给服务端，服务端拿到id和存储在服务器的id进行对比，成功则登录，不成功则重定向
'''

import requests

#r=requests.post(url="http://test.admin.jlncjy.cacfintech.com/api/v1.0/chanquan/user/login")

def login(url="http://test.admin.jlncjy.cacfintech.com/api/v1.0/chanquan/user/login"):
    params={"username":"18811112224","password":"123456"}
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
             "Referer":"http://test.admin.jlncjy.cacfintech.com/",
             "Content-Type":"application/json;charset=UTF-8"}
    r=requests.post(
        url=url,json=params,headers=headers
    )
    return r.cookies
    print(r.json())
    #这样就拿到了sessionid
    print(r.cookies)

#缺少部分入参
def profile():
    r=requests.post(url='http://test.admin.jlncjy.cacfintech.com/api/v1.0/chanquan/project/selectMobileLandList',
                    cookies=login())
    print(r.json())
profile()