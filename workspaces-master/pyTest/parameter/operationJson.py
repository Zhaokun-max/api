import json


def readJson():
    return json.load(open("login.json","r",encoding='utf-8'))['item']

#循环遍历
# for item in readJson():
#     print(item)
