import json
import requests

# 把python的数据类型转换为str类型
# 反序列化：把str类型转为python数据类型结构


#请求网站返回json文件，对json文件进行处理为字典，根据字典进行遍历，根据遍历mobile修改手机号
r = requests.post(url='http://test.admin.jlncjy.cacfintech.com/api/v1.0/chanquan/user/login',
                  headers={'Content-Type':'application/json;charset=UTF-8',
                           'Cookie':'test.rongxin.chanquan.admin.jilin.sid=s%3Atest.rongxin.chanquan.admin.jilin.sid%3A-YGWGjhsxOuei3ieDYsiYz_gcmZ3bOmG.%2F5UF%2F6Ae%2FGixCwcEKBOSbriKUcTsZLgomBygrhBedKs.rongxin.chanquan.admin.jilin.sid=s%3Atest.rongxin.chanquan.admin.jilin.sid%3A-YGWGjhsxOuei3ieDYsiYz_gcmZ3bOmG.%2F5UF%2F6Ae%2FGixCwcEKBOSbriKUcTsZLgomBygrhBedKs',
                           'Referer':'http://test.admin.jlncjy.cacfintech.com/',
                           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                           'Connection': 'keep-alive',
                           },
                  data=json.dumps({"username":"18811112224","password":"123456"})
                  )
rl=r.text
r=json.loads(rl)
#print(r)
#print(type(r.text))

#遍历
dic ={}
def json_txt(r):
    if isinstance(r,dict): #判断是否是字典类型isinstance 返回True false
       for key in r:
            if isinstance(r[key],dict):#如果dic_json[key]依旧是字典类型
                print("key--：%s value--: %s"%(key,r[key]))
                json_txt(r[key])
                dic[key] = r[key]
            else:
                print("key：%s ****value--: %s"%(key,r[key]))
                dic[key] = r[key]

json_txt(r)
print("dic ---: "+str(dic))
# json_txt(r)


#修改手机号，遍历json字典key值后，比对如果遍历到对于的key则修改其value
def  check_json_value(dic_json,k,v):
    if isinstance(dic_json,dict):
        for key in dic_json:
            if key == k:
                dic_json[key] = v
            elif isinstance(dic_json[key],dict):
                check_json_value(dic_json[key],k,v)
# print("date_json 变更前   :")
# print(date_json)
check_json_value(date_json,'mobileTel','13333333333')
print("date_json 变更后   :")
print(date_json)

#print(list1)
#print(type(list1))

#返回状态码code
#print(r.status_code)


'''
# dict2 = {'name':'panda','age':'18'}
# #序列化：dict---->str
# dict_str=json.dumps(dict2)
# print('序列化结果:',dict_str)
# print(type(dict_str))
#
#
# # 反序列化
# str_dict = json.loads(dict_str)
# print('反序列化结果:',str_dict)
# print(type(str_dict))
#
#
#
# #列表的序列化与反序列化过程'''
#
# list1=['123','sdasa','admin']
# list2=json.dumps(list1)
# print('序列化结果:',list2,type(list2))
#
# # 反序列化
# list3=json.loads(list2)
# print('反序列化结果:',list3,type(list3))
#
#
# #元组序列化与反序列化过程'''
#
# tuple1=('a','b','c')
# tuple_1=json.dumps(tuple1)
# print('序列化结果:',tuple_1,type(tuple_1))
#
# # 不会变回元组，编程列表
# tuple_2=json.loads(tuple_1)
# print('反序列化结果:',tuple_2,type(tuple_2))

'''文件的序列化与反序列化'''

# r=requests.get(url='http://www.weather.com.cn/textFC/hb.shtml#')
#
# # print(r.content.decode('utf-8'))
# #print(type(r.text))
#
# #对文件进行序列化--->就是把服务器的响应数据写到文件中
# json.dump(r.content.decode('utf-8'),open('weather.json','w'))
#
# #对文件反序列化，就是读取文件的内容
# dict1=json.load(open('weather.json',encoding='utf-8',mode='r'))
# print(dict1)
# print(type(dict1))


'''
1.文件反序列化后，类型是unicode
2.运行编码，把unicode类型转化为str
3.str类型进行反序列化后，转换成字典类型
dict1=json.loads((json.load(open('dd.json','r'))).encode('utf-8')

'''