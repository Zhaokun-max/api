


#登录

import requests


def login():
    s=requests.Session()
    url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021032259446'
    data={'email':'13693689954','icode':'','origURL':'http://www.renren.com/home',
          'domain':'renren.com','key_id':'1','captcha_type':'web_login',
          'password':'66c479fcdcf98146e021ce8bf614560351b4902edb951bb0ae4fcb4d56f5c4bb',
          'rkey':'d0cf42c2d3d337f9e5d14083f2d52cb2',
          'f':'http%3A%2F%2Fwww.renren.com%2F877521005'}
    headers={'Content-Type':'application/x-www-form-urlencoded',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


    r=s.post(url=url,data=data,headers=headers)
    return s
#登录成功进入个人主页
def profile():
    r=login().get(url='http://www.renren.com/877521005')
    print(r.text)

#上传照片接口
def upload():
    url='http://upload.renren.com/upload.fcgi?pagetype=nphoto&hostid=877521005&uploadid=1609943209084'
    data={'requestToken':'772812890','_rtk':'f9d12eb4'}
    files={'file':('login.yaml.jpg',open(r'C:\Users\Administrator\Desktop\20a259868d31ebaa482a6dd4da46652.png','rb'),'image/jpeg',{})}
    headers={'Content-Type':'multipart/form-data'}
    r=login().post(url=url,data=data,files=files,headers=headers)
