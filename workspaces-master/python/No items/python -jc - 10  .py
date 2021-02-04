"""
定义一个学生类，用来描述学生的

"""


# 定义一个空的类
class Student():
    # 一个空类，pass代表跳过
    # 此处psaa必须有
    pass


# 定义一个对象
panda = Student


# 在定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"

    # 需要注意
    # 1.def Dohomework的缩进层级
    # self系统默认参数

    def Dohomework(self):
        print("做作业")
        # 在函数末尾使用return语句
        return None

# 实例化一个叫panda的学生，是一个具体人
panda = PythonStudent()
print(panda.name)
print(panda.age)
# 注意成员函数的调用没有传递参数
panda.Dohomework()
