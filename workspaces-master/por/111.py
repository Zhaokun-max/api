
# import requests
# headers = {
#             #'Content-Type': 'application/json;charset=UTF-8',
#             'Cookie': 'test.rongxin.chanquan.portal.jilin.sid=s%3Atest.rongxin.chanquan.portal.jilin.sid%3ASKPIQZaa3Ly9qOrarHNpU9yUy658RM9U.NYALLk87ohTco%2Bf5XWKAfkuHv36HjTqo6Qeahrc7Qck',
#             #'Referer': 'http://test.portal.jlncjy.cacfintech.com/',
#             #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#             #'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHAiOiJQQyIsInN1YiI6Ijg2IiwiYXVkIjoicm9uZ3hpbjpjaGFucXVhbjpqd3Q6YWNjZXNzIiwic2NvcGUiOiJ0ZXN0OnJvbmd4aW46Y2hhbnF1YW4iLCJpc3MiOiJST05HWElOX0NIQU5RVUFOIiwidHlwZSI6MywiZXhwIjoxNjEzMTIxNzQyLCJvd3QiOiJ1c2VyIn0.2HfnHqJY-GtYXN9VggIOaXSzIKUxbju664WtsBz8Eao',
# }
# url = "http://test.portal.jlncjy.cacfintech.com/api/v1.0/chanquan/fast/uploadFile"
#
# files={"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg"),}
# data={'bizType':'','width':'1024','height':'768','Content-Disposition':'form-data'}
# for i in range(10):
#
#     r = requests.post(url, files=files,headers=headers)
#     print(r.json())
import json
def read_photo():
    with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
       return f.readlines()

def re():
    line=json.dumps(read_photo())
    line1=json.loads(line)
    #line1=list(line)
    print(line1[7])

import random
for i in range(10):
    s=random.randrange(1,30000)
    print(s)
def a():

    i=random.randrange(1,8)
    print(i)
    if i ==1:
        return '农村土地转让200亩地'
    if i ==2:
        return '这是一个生成的流转类型'
    if i ==3:
        return '关于蔡家镇的流转补贴'
    if i ==4:
        return '关于蔡家镇政府的项目'
    if i ==5:
        return '个人流转项目以及介绍'
    if i ==6:
        return '这是无尽空虚'
    if i ==7:
        return '情人大地'
    if i ==8:
        return '在那些苍翠的路上'
def b(a):
    p = random.randrange(1, 1000)
    s=a()+str(p)
    print(s)


b(a)



