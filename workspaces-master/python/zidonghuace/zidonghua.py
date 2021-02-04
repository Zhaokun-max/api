def key_values_to_dic(key_values):
    """
    将键值对转换为字典形式
    :param key_values_:
    :return:
    """
    key_values_dic_ = {}
    for line in key_values.split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            key, value = line.split(":", 1)
            key = key.strip()
            key_values_dic_[key] = value
        except ValueError:
            print("ERROR: 键值对错误，转换失败", line)
    return key_values_dic_


key_values = """
content: {pageNo: 1, pageSize: 30, totalPage: 10, expectPositionName: null, showId: null,…}
expectPositionName: null
pageNo: 1
pageSize: 30
positionList: [{positionId: 7875046, companyId: 370487, positionName: "测试工程师",…},…]
0: {positionId: 7875046, companyId: 370487, positionName: "测试工程师",…}
adCode: null
adId: null
businessZone: "望京"
city: "北京"
closeIcon: null
collectionTime: 0
companyFullName: "北京青岳科技有限公司"
companyId: 370487
companyLogo: "https://www.lgstatic.com/thumbnail_360x360/i/image3/M00/51/4B/CgpOIFr9CRSARnF2AAAcvkuFHT8882.png"
companyName: "青岳科技"
companySize: "50-150人"
companyToplistSummaries: null
cornerTag: null
cornerType: null
createTime: 1605258329000
distance: null
district: "朝阳区"
education: "本科"
financeStage: "未融资"
hasCollect: false
hasDeliverResume: false
hasOptions: null
hasStock: null
hiTags: null
hrCardVo: null
hrId: null
imageUrl: null
index: null
industryField: "移动互联网"
infoLink: null
isDirect: false
isSchoolJob: false
isTop: null
jobNature: "全职"
positionAddress: "广顺北大街福码大厦B座16层"
positionAdvantage: "团队优秀，六险一金，近地铁"
positionId: 7875046

"""
print(key_values_to_dic(key_values))



#  取列表中的字段

dict2 = {"key":[{"key":100},{"b":2}]}

for i in dict2["key"]:
    print(i)

#获取列表中的字典并打印kv
dict3 = {"key":[{"key":100},{"b":2}]}

for i in dict3["key"]:
    for k,v in i.items():
        # 判断如果某个值在字典里面 则打印pass
        #if "key" in i :
           # print("pass")
        #else:
        #print("1111")
        print(k,':',v)



#取出列表下 所有字典中的同一个字段数据

dict4 = {"key":[{"key":100},{"b":2.3}]}

for i in dict4["key"]:
    for k,v in i.items():
        if "key" in i:
            if k == 'key':
                print(k,":",v)
                print(v)

# 取出的值整数显示
dict5 = {"key":[{"key":100.2},{"b":2.3}]}

for i in dict5["key"]:
    for k,v in i.items():
        if "key" in i:
            if k == "key":
                print(int(v))


# 分割 和拼接

lis = "9.6"
list_1 = lis.split(".")
print(list_1)

list2 = ".".join(list_1)
print(list2)


#字典转为列表

dict1 = {"key":1,"values":2}
dict2 = list(dict1.keys())
print(dict2)

#数据驱动中  data的目录下(.txt，csv, xml, config)

def data_dir(filepath = "d:/data", fileName=None):
    print(filepath)#d:/data
    print(fileName)#test.txt


data_dir(fileName="test.txt")



# 默认登录


def login(username="admin",pasword="123"):
    pass
#换其他账号重新复制
login("")


# 动态参数  对请求参数进行ascill排序

#ddt模块  学
# 收集参数  arg 列表   kwargs
def long(*args, **kwargs):
    print(args, kwargs)

long(2)
long(name="xiaoming")
long("a")

# 需求
# 1.对请求参数进行acsill排序
# 2.排序后对请求参数进行md5加密

#写一个函数，获取请求参数，对请求参数进行加密


def date(**kwargs):
    return dict(sorted(kwargs.items(),key=lambda item:item[0]))

dictw = {"name":"panda", "age":180, "genrd":"women"}
print(date(**dictw))



#登录返回session
def login():
    username = input("请输入登录用户名")
    password = input("请输入密码")
    if username == "panda" and password == "12345":
        return "session"

def proin(session):
    if session == login():
        print("denglu个人中心")
    else:
        print("过期")

proin("session")


#封闭：已经实现的功能代码尽量不要修改
#开放；对现有的功能代码可扩展
#需求：在调用 f1或f2的时候，先打印python自动化测试实战，在打印XX平台
def log(func):#f1相当于log的参数   执行内部函数  执行完成后参数f1进入log函数执行f1
    def inner():

        print("zuid2ghuashizhan ")
        func()# 相当于执行f1
    return inner
@log   #装饰器 先执行装饰内容 在执行被执行  被执行为f1
def f1():
    print("xxpingtai")

def f2():
    print("xx")

f1()

"""
1.执行log函数的时候，把被装饰的函数f1当做参数来传递
2.getinfo函数的返回值会重新赋值
3.一旦结合了装饰器后，调用f1的函数其实执行的是inner函数的内容。原来f1的函数会被覆盖
4.被装饰的函数f1重新赋值给装饰器的内层函数inner

"""



















