'''配置文件的操作'''
import configparser
import os

def base_dir(filename=None):
    #当前目录下
    #return os.path.dirname(__file__)
    return os.path.join(os.path.dirname(__file__),filename)

def getlinux(linux='linux'):
    #进行实例化
    list1=[]
    config=configparser.ConfigParser()
    cp=config.read(base_dir('config.ini'))
    ip=config.get(linux,'IP')
    port=config.get(linux,'PORT')
    username=config.get(linux,'USERNAME')
    password=config.get(linux,'PASSWORD')
    list1.append(ip)
    list1.append(port)
    list1.append(username)
    list1.append(password)
    return list1

print(getlinux()[0])


