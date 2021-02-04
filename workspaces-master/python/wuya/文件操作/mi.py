#给用户三次机会，猜想我们程序生成一个数字A，每次用户猜想过后提示数字是否正确
# 以及用户数字是大还是小于A，当机会用尽时提示用户已经输掉了

import random
#
# r=random.randint(1,100)
# print(r)
# times=3
#
# while times:
#     num = input("请输入数字")
#     if num.isdigit():
#         num=int(num)
#         if num==r:
#             print('对了')
#             break
#         elif num>r:
#             print('大了')
#             times=times-1
#         else:
#             print('小了')
#             times=times-1
#     else:
#         print("请输入整数")
#         times=times-1
# print('结束')


# x=0
# while x<1000:
#     if x % 2 == 1 and x % 3 == 2 and x % 5 ==4 and x % 6 == 5 and x % 7 == 0:
#         print(x)
#         x+=1
#     else:
#         x+=1   # 不加1 则直接打印出循环内的1000个 进入死循环  数字加1后到1000结束循环


# 设计一个验证用户密码的程序，用户只有三次将会输入密码，不过如果用户输入的内容包括“”则不计算

# password="123"
#
# time=3
#
# while time:
#     out=input('请输入密码')
#
#     if "*" in out:
#         print('不能输入特殊字符')
#         time=time-1
#     else:
#         if out==password:
#             print('成功')
#             break
#         else:
#             print("密码错误")
#             time=time-1








'''
1.创建用户名保存到文件夹
2.登录成功后进入个人中心

管理用于登录系统的用户信息，登录名字和密码，
登录用户账号建立后，以保存用户可以登录名字和密码重返系统，
新用户不能用别人的用户名建立用户账号

'''
import json
import sys
def Input():
    username=input('请输入账户\n')
    password=input('请输入密码\n')
    return username,password


def resat():
    username,password=Input()
    as1=json.load(open("longin","r"))
    info=as1.split('|')
    if info[0]==username:
        print('该账户已经注册')
    else:
        temp=username+'|'+password
        json.dump(temp,open("longin","w"))
        print('恭喜你，注册成功')



def login():
    username,password=Input()
    as1=json.load(open("longin","r"))
    info=as1.split('|')
    if info[0] != username:
        print('账户不存在')

        sys.exit()
    else:
        if info[0]==username and info[1]==password:
            return True
        else:
            return False

def getnick(func):
    as1=json.load(open("longin","r"))
    info=as1.split("|")
    if func:
        print("{0},欢迎登录系统".format(info[0]))

        sys.exit()

    else:
        print('账户或密码错误，请重新登录')


if __name__ == '__main__':
    while True:
        try:
            lin=int(input("1.注册，2.登录 3.退出系统\n"))
            if lin==1:
                resat()
            elif lin==2:
                getnick(login())
            elif lin==3:
                break
            else:
                print('错误')
        except Exception as f:
            f.args
            print('请输入正确的数字')
    print('欢迎下次使用')