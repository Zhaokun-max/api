'''
类：类是由一些列属性和方法组成
'''
# class F1(object):
#     pass

'''
f2=F1()
对象的创建 -->就是类实例化的过程
一个特性：
1.对象的句柄，区分不同的对象
2.属性
    -私有属性
        类属性  它属于类也属于对象,建议使用类调用
        实例属性  它只属于对象
        局部变量
    -共有属性
3.方法

'''

# class Person(object):
#
#     Earth='China'
#     def __init__(self,name,age):
#         #实例属性
#         self.name=name
#         self.age=age
#         zone='空间'
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#     def setName(self,name):
#         self.name=name
#
#     def setAge(self,age):
#         self.age=age
#
#     def info(self):
#         return 'name is {}, age {}, 来自{}'.format(self.getName(),self.age,self.Earth)

#p=Person('panda',18)
# p2=Person('tain',19)
# #print(p.getName())
# p2.setAge(18)
# p2.setName('lisy')
# #p2.setAge('18')
# #print(p2.getName())
#
#print(p2.info())
#类调用共有变量
# print(Person.Earth)

# #args
# class Person():
#     def __init__(self,*args,**kwargs):
#
#         self.kwargs=kwargs
#         self.args=args
#     def info(self):
#         return self.kwargs,self.args
#
# per=Person(name='panda')
# print(per.info())
#
# pr2=Person(name='xiao',age=18)
# print(pr2.info())
# #输出结果包括()或者{} 因为args和keargs同在
# pr3=Person("xin",12)
#print(pr3.info())

'''
一个类，不管是否写了构造函数，它都是有构造函数的
构造函数
1.初始化属性
2.一个类可以有多个构造函数  建议一个类有一个构造函数
'''

# class Person(object):
#     #初始化
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __init__(self,address):
#         self.address=address
#
# p=Person('panda',8)


'''
析构函数
对象实例化-->构造函数-->对象调用方法-->
代码调到具体的方法-->执行方法的代码块-->
最后执行析构函数
'''
# class Person(object):
#     #初始化
#     def __init__(self):
#        print('我是构造函数')
#     def __del__(self):
#         print('我是析构函数')
#     def info(self):
#         print('我是方法')
#
# p=Person()
# p.info()


'''
普通方法
特性方法
'''
# class Person(object):
# #链接mysql
#     def coon(self,user,password,host,):
#         pass
#     def fi(self,*args,**kwargs):
#         pass
#     def info(self):
#         print('普通方法')


# p1=Person()
# p1.coon("panda","1234","3368")
#
# p1.fi(12)
# p1.fi("admin")
# p1.fi(name=19)

'''
特性方法  这个方法不能有形势参数
'''
# class Person():
#
#     @property
#     def userId(self):
#         pass
# #特性方法不需要括号
# p1=Person()
# p1.userId


'''
静态方法：直接使用类名进行调用，它属于类
对象也可以调用静态方法，建议不这样写
'''
# #链接mysql
# class Mysql(object):
#     @staticmethod
#
#     def coon(user):
#         pass
# Mysql.coon("panda")


'''
类方法：直接使用类进行调用，属于类
'''

# class Person():
#     @classmethod
#     def coon(cls):
#         pass

'''
属于类：
    类属性
    静态方法
    类方法
属于对象：
        实例属性
        普通方法
        特性方法
'''


'''
继承：重用已经存在的数据和行为，减少代码重复编写
子类继承父类所有的实例变量和方法
'''
'''
类属性的继承
'''
# class Person(object):
#     china='diqiu'
#
# class usaPerson(Person):
#     pass
#
# pre=usaPerson()
# pre.china

'''
实例属性的继承和继承的两种写法

'''
# class Fruit(object):
#     def __init__(self,name):
#         self.name=name
#
# class Apple(Fruit):
#     def __init__(self,name,banrd,cools):
#         super(Apple,self).__init__(name)
#         #Fruit.__init__(self,name)
#         self.banrd=banrd
#         self.cools=cools
#
#     def info(self):
#         print("名字是{}，品牌是{}，颜色为{}".format(self.name,self.banrd,self.cools))
#
# apple=Apple("12x","苹果","红色")
#apple.info()

'''
由于需求，不需要继承父类的实例属性
只打印品牌颜色
'''
# class Apple(Fruit):
#     def __init__(self,banrd,cools):
#         self.banrd=banrd
#         self.cools=cools
#
#     def info(self):
#         print("品牌是{}，颜色为{}".format(self.banrd,self.cools))
#
# apple=Apple("苹果","红色")
# apple.info()


'''
方法的继承
1.子类为什么重写父类的方法：子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类
调用的方法(父类，子类都存在)，执行的的是子类的方法

单个类继承的原则
1.从上到下，子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后调用的方式是父类的方法
2.从下岛上，子类继承父类，子类重写了父类的方法，那么子类实例化后，子类优先调用自己的方法

'''
# class Fruit(object):
#     def eat(self):
#         print('可以吃')
#
# class chinaApple(Fruit):
#     def __init__(self,cools):
#         self.cools=cools
#     def eat(self):
#         print('苹果{}可以吃'.format(self.cools))
#
# class usaApple(chinaApple):
#     def eat(self):
#         print('usaAple')
#
# usa=usaApple("hongse")
# usa.eat()


'''
多个类的继承，从左到右的原则
'''
# class Person(object):
#     def eat(self):
#         print('chu')
#
#
# class monther(Person):
#     def eat(self):
#         print('chi')
#
# class father(Person):
#     def eat(self):
#         print('he')
# #不能同时与父类和父类的父类同时继承
# class son(father,monther):
#     def wan(self):
#         print('1')
#
# p=son()
# p.eat()

#登录
# import json
# import sys
# class log(object):
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
#
#
#     def getusername(self):
#         return username
#     def setpassword(self):
#         self.username=username
#     def getpassword(self):
#         return password
#     def setpassword(self):
#         self.password=password
#
#     def reginer(self):
#         temp=self.username+"|"+self.password
#         json.dump(temp,open("aa","w"))
#     def login.yaml(self):
#         f=json.load(open('aa','r'))
#
#         f=f.split("|")
#
#         if f[0]==self.username and f[1]==self.password:
#             return True
#         else:
#             return False
#     def userinfo(self):
#         f=json.load(open('aa','r'))
#         f=f.split("|")
#
#         r=self.login.yaml()
#         if r:
#             print('恭喜你{}登录成功'.format(f[0]))
#
#         else:
#             print('登录失败')
#     def exit(self):
#         sys.exit()
#
# def main():
#     per=log('panda','123456')
#
#     while True:
#         try:
#             inp=int(input("1.注册 2.登录 3.退出\n"))
#         except Exception as f:
#             print('输入信息错误')
#         else:
#             if inp==1:
#                 per.reginer()
#             if inp==2:
#                 per.userinfo()
#             if inp==3:
#                 per.exit()
#
# if __name__ == '__main__':
#     main()

'''
__doc__ 打印出类的注释
'''
# class Person(object):
#     '''对人的定义'''
#     def info(self,username,password):
#         pass
# print(Person.__doc__)

'''__call__:对象创建时直接返回__call__内容，使用该方法可以模拟静态方法'''
#
# class P1(object):
#     def __new__(cls, *args, **kwargs):
#         print('call方法')
#
# per=P1()

'''__str__：对象代表的含义，返回一个字符串，通过它可以把对象和字符串关联起来，方便某些程序的实现
该字符串表示某个类，实现了__str__后，可直接使用print语句输出对象，也可以
通过函数str来触发__str__的执行
1.对象的意思
2.返回一个字符串，字符串和对象关联起来，该字符串表示某个类
'''

# class son(object):
#     '''beizhu'''
#     def __str__(self):
#         return self.__doc__
#
# s=son()
# print(str(s))

class Factroy(object):
    def createFruit(self,fruit):
        if fruit=='apple':
            return Apple()
        elif fruit=='banana':
            return Banana()
class Fruit(object):
    def __str__(self):
        return 'fruit'
class Apple(Fruit):
    def __str__(self):
        return 'apple1'
class Banana(Fruit):
    def __str__(self):
        return 'banana'

if __name__ == '__main__':
    factroy=Factroy()
    print(factroy.createFruit('apple'))



