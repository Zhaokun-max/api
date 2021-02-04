'''
访问系统返回
基本认证
常规认证
自定义认证
都需要鉴权
'''

import requests
#基本认证basic
from requests.auth import HTTPBasicAuth

r=requests.get(url='http://127.0.0.1:5000/v1/api/books',auth=('admin','admin'))
#auth另一种写法，auth=HTTPBasicAuth('admin','admin')  admin 是用户名和密码
print(r.text)