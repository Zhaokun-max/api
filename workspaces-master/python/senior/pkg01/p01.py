#定义一个学生类
#一个sayhello函数
#一个打印语句
class Student():
    def __init__(self, name="padda", age=19):
        self.name = name
        self.age =age

    def say(self):
        print("my name is {}".format(self.name))

def sayhello():
    print("hi, 想干啥")
s=Student()
s.say()
print('嗯哼')