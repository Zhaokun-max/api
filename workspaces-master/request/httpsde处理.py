
import requests

r=requests.get(url='https://www.wuya.com/',verify=True)
print(r.text)


#如果发送https带verify关键怎么处理
#如果访问网站返回verify或者CA的时候
#第一种：把证书的路径带上
#第二种：verify=True





