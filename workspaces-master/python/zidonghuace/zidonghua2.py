# 需求：要求注册账户，然后注册的账户登录到系统后，显示出登录的昵称
# 1.注册的函数
# 2.登录的函数
# 3.获取昵称的函数


import json
import sys
def inout():
    username = input("请输入账户：\n")
    password = input("请输入密码：\n")
    return username,password

def register():
    """
    实现账户注册的功能
    :return:
    """
    username,password=inout()
    temp = username+'|'+password
   # with open('login.yaml.txt','w') as f:
        # f.write(temp)
    #反序列化
    json.dump(temp,open('user','w'))

def login():
    "登录的函数"
    username,password=inout()
    # with open("login.yaml.txt","r") as f:
    #     info = f.read()
    # 序列化文件
    #扩展   for循环把str转换成列表，切割，根据下标进行判断
    lsogn=json.load(open('user','r'))

    info = lsogn.split("|")
    if username==info[0] and password==info[1]:

        return True

    else:
        return False


    # if username ==  [0] and password==info[1]:
    #         return True
    # else:
    # return False


def getnick(func):
    "获取昵称"
    # with open("login.yaml","r") as f:
    #     info = f.read()
    # info = info.split('|')
    lsogn=json.load(open('user','r'))
    info = lsogn.split("|")
    if func:  #func==True
        print('{0}，你好，欢迎登录XX系统'.format(info[0]))
    else:
        print('请登录系统')


if __name__ == '__main__':
    #2.7  he 3.0  存在版本差异
    while True:
        try:
            t = int(input('1.注册 2.登录 3.退出系统\n'))

            # 判断小数类型
            if isinstance(t,float):

                t=int(t)
            # 判断字符串类型
            elif isinstance(t,str):
                # 判断字符串是否大于1位
                if len(t)==1:
                    #把字母转换成数字
                    t=ord(t)
                    # 如果是多个字母的话，判断下边取值
                else:
                    t=int(ord(list(t)[0]))

        except Exception as f:
            print(f.args)

        else:
            if t==1:
                register()
            elif t==2:
                getnick(login())
            elif t==3:
                sys.exit()
            else:
                print('输入错误')
        finally:
            pass


