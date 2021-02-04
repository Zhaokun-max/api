

import requests

# r=requests.get(
#     url='http://httpbin.org/get',
#     params=None
# )
# print("请求地址：",r.url)
# print("响应头:",r.headers)
# print('json格式的数据：',r.json())
# print('基于文本的数据',r.text)
# print('二进制的内容：',r.content)
# print('状态码:',r.status_code)
# print('cookies：',r.cookies.get_dict('sessionID'))
# print('cookies：',r.cookies.get_dict())
# print('cookies：',r.cookies)
'''
r.json的错误演示
区别返回值是否为html或者json格式  如果不是json格式的话调用r.json会报错
需使用r.text

'''
# r=requests.get(url='http://www.baidu.com')
# print(r.status_code)
# print(r.text)
#如果r.text返回的是乱码或者二进制的话使用content
'''
r.content演示
'''
#r=requests.get(url='http://www.weather.com.cn/')
#使用text会有乱码
#print(r.text)
#使用content
#什么类型的编码使用什么样的编码格式  gbk
#print(r.content.decode('utf-8'))

'''
r.cookies
'''
# r=requests.get(url='http://www.weather.com.cn/')
# print(r.cookies.get_dict())

