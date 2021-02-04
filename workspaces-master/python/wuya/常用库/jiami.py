'''
1.对请求参数进行ASCII的排序
2.做url  encode编码：name=panda&age=18&city=xian
3.做md5---> sign--->4cc040a4ab1daf65b0ac1cbda4bd1b91

'''
dict1={'name':'panda','age':'18','city':'xian','work':'taert'}

dict2=dict(sorted(dict1.items(),key=lambda item:item[0]))

from urllib import parse

datas=parse.urlencode(dict2)
#print(datas)


import hashlib

def md5(**kwargs):
    dict2=dict(sorted(dict1.items(),key=lambda item:item[0]))
    datas=parse.urlencode(dict2)
    md5=hashlib.md5()
    md5.update(datas.encode('utf-8'))
    return md5.hexdigest()

print(md5(name='panda'))