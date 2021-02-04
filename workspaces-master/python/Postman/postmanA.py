

import json
import requests


def readJson():
    #json文件转为字典类型
    # file = open('dd.json',encoding='utf-8',mode='r')
    # info = json.load(file)
    return json.load(open('dd.json',encoding='utf-8',mode='r'))
#字典类型
#print(type(readJson()))
#print(readJson()['item'][0]['request']['url']['raw'])

# print(type(readJson()['item'][0]['request']['method']))
# # 打印出的是字符串
# def one_get():
#     for i in readJson()["item"]:
#         if item["request"]["method"]=="GET":
#            print(readJson()['item'][1]['request']['method'])
#        elif item["request"]["method"]=="POST":
#            pass
#
# one_get()
def one_get():


    r=requests.request(method=readJson()['item'][0]['request']['method'],
                       url=readJson()['item'][0]['request']['url']['raw'])
    #print(r.json())#报错原因存在返回不是json文件，需要接口返回数据，不是网址
    s=r.json()
    print(s)

    # s=r.text
    # print(s)


one_get()