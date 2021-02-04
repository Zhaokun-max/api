#实现思路 pytestconfig读取自定义命令行的选项 然后pytest自动解析需要hoop函数
#关联conftest里面pytest_addoption函数
#命令pytest -s -v test_oe.py --foo=a 也可以=号  a代表打印出的值
#自定义参数选项
import requests
def test_first(getfoo):
    print(getfoo)

#登录
def test_login_auth(username,password):
    dict={'username':username,'password':password}
    r=requests.post(
        url='http://127.0.0.1:5000/auth',
        json=dict
    )
    print('\n响应结果信息',r.json())


#catch
def test_taobao():
    #设置timeout0.01秒内响应如果没响应报错
    #如果是接口出错，先执行失败的用例
    #pytest -s -v test_oe.py --tb=no --failed-first  如果有失败的这种执行方式可以减少报错信息
    #pytest -s -v test_oe.py --tb=no --last-failed  先执行失败的用例
    #回顾错误信息pytest --cache-show  记录对应的信息
    # 既不是产品的问题也不是代码问题，可以catch执行查看原因
    r=requests.get(url='http://taobao.com',timeout=0.01)
    #响应时间
    print("响应时间",r.elapsed.total_seconds())



#io临时文件操作
