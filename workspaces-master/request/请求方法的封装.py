
'''
必不可少
请求方法
请求地址
封装思路：
有方法 有地址，**kwargs思路解决
'''
import requests
#
# class Method:
#     def get(self, url, **kwargs):
#         try:
#             return requests.get(url=url,**kwargs)
#         except BaseException as e:
#             return e.args[0]
#         # except:
#         #     raise '接口请求错误'
#
#     def post(self, url, **kwargs):
#         try:
#             return requests.post(url=url, **kwargs)
#         except BaseException as e:
#             return e.args[0]
#
#
# url='http://www.renren.com/ajaxLogin/login'
# data={'email':'13693689954','icode':'','origURL':'http://www.renren.com/home',
#           'domain':'renren.com','key_id':'1','captcha_type':'web_login',
#           'password':'66c479fcdcf98146e021ce8bf614560351b4902edb951bb0ae4fcb4d56f5c4bb',
#           'rkey':'d0cf42c2d3d337f9e5d14083f2d52cb2',
#           'f':'http%3A%2F%2Fwww.renren.com%2F877521005'}
# headers={'Content-Type':'application/x-www-form-urlencoded',
#              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
#
# obj=Method()
# r=obj.post(url=url, data=data, headers=headers)
# print(r.text)


'''
第二种封装思路
'''
class Requests:
    def request(self,url, method='get', **kwargs):
        if method=='get':
            return requests.request(url=url, method=method, **kwargs)
        elif method=='post':
            return requests.request(url=url, method=method, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url=url, **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method='post', **kwargs)

url='http://www.renren.com/ajaxLogin/login'
data={'email':'13693689954','icode':'','origURL':'http://www.renren.com/home',
          'domain':'renren.com','key_id':'1','captcha_type':'web_login',
          'password':'66c479fcdcf98146e021ce8bf614560351b4902edb951bb0ae4fcb4d56f5c4bb',
          'rkey':'d0cf42c2d3d337f9e5d14083f2d52cb2',
          'f':'http%3A%2F%2Fwww.renren.com%2F877521005'}
headers={'Content-Type':'application/x-www-form-urlencoded',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
obj=Requests()
r=obj.post(url=url, data=data, headers=headers)
print(r.status_code)
print(r.text)


