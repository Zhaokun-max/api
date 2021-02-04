

import requests
# 如果请求的数据格式不是json，但是使用json参数，会报参数缺失
#data针对from表单
#json针对序列化数据
# application/x-www-from-urlencode--》  使用data参数  不能使用json
# application/json-》json格式的字符串的数据类型--》字符串 可以使用data也可以使用json
#
# data={"mobileCode":"1350000000","userID":""}
# headers={"Content-Type":"application/x-www-form-urlencoded"}
# r=requests.post(url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
#                 json=data,headers=headers)
# print(r.text)

'''
使用json
1.满足的要求而“application/json-->json格式的字符串
2.请求参数必须是字段
但是2必须在1的条件下才可以
data
1.数据格式是字典，但不满足请求方式
'''
#
# import json
# headers={"Content-Type":"application/json"}
# data={"author":"无涯","done":True,"name":"API测试实战"}
# r=requests.post(url='http://127.0.0.1:5000/v1/api/books',
#                 data=json.dumps(data),
#                 headers=headers)
#
# print(r.text)




'''
url=www.wuya.com
字典嵌套列表，列表中嵌套字典处理
data={'name':'wuya','age':18,"data":[{''}]}
'''
import json
#特殊的json格式
#json格式的字符串---》str，但是还有列表类型需要处理
datas={'name':'wuya','age':18,'data':[{'address':'xian'}]}

headers={'content-type':'application'}
#处理json中的列表
datas['data']=json.dumps(datas['data'])
r=requests.post(url='这是地址',json=datas,headers=headers)
#请求请求参数错误或其他500的错误
#需要对data进行处理
