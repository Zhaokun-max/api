#定义一个学生类
#一个sayhello函数
#一个打印语句
class Student():
    def __init__(self, name='22', age=19):
        self.name = name
        self.age =age

    def say(self):
        print("my name is {}".format(self.name))

def sayhello():
    print("hi, 想干啥")

# 判断语句作为程序入口
if __name__== '__main__':
    stu=Student()
    stu.say()
    print('enheng')