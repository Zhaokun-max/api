

'''
固定时间----》time
响应时间=请求时间+响应返回客户端的时间
请求timeout怎么处理
可以加timeout处理
'''
import requests

r=requests.get('http://httpbin.org/get',timeout=0.0001)
print(r.text)