import math
"""print(math)
# celi() 向上取整操作
print(math.ceil(5.01))
print(math.ceil(6.01))

#floor()向下取整
print(math.floor(6.01))
print(math.floor(6.9))
"""
# 查看系统保留关键字 不可用来当做变量名
"""import keyword
print(keyword.kwlist)"""

# round 四舍五入操作  python  内置函数
"""print(round(5.01))
print(round(5.9))
# sqrt 开平方 返回浮点数
print(math.sqrt(4))"""

# pow() 与幂运算差不读，计算一个数的几次方  由两个参数，第一个是底数，第二个指数
"""print(math.pow(3,2))  # 三的二次方
# 幂运算
print(3**2)#返回浮点数 返回整数"""

# fabs（）  对一个数值获他的绝对值  返回浮点数
"""print(math.fabs(3))
print(math.fabs(-1))
#abs()  获取绝对值操作  不是数学模块当中的 是python内置函数 返回值由本身类型而定
print(abs(1))
print(abs(2.5))

# fasum() 求和 对整个序列求和  返回浮点数
print(math.fsum([1,2,3,6]))
# sum（） python内置求和  返回整数
print(sum([1,2,3,6]))

# math.modf() 讲一个浮点数拆分为整数部分和小数部分组成元组  小数在前 整数在后
print(math.modf(4.5))
print(math.modf(3))
print(type(math.modf(0)))
help(math.modf)
#copysign  将第二个数的符号 (正负号)传给第一个数  返回第一个数的浮点数
print(math.copysign(2,-6))
print(math.copysign(-5,1))
# 打印
int(math.e)
print(math.pi)"""

import random
# random  获取0-1 之间的随机小数 包含0不包含1
# for i in range(10):
    #print(random.random())
    #随机指定开始和结束之间的值
    # print(random.randint(1,9))
    # random.randrange  获取指定开始和结束之间的值  可以指定间隔值
    #     print(random.randrange(1,5,2))
# uniform() 随机获取指定范围内的整数值 ， 包括小数
#     print(random.uniform(1,9))
# choice()  随机获取列表中的值  内置函数
# print(random.choice([1,52,1,3,6,8,6]))

# # shuffle  随机打乱序列
# list1 = [1,5,9,2,00]
# print(list1)
# random.shuffle(list1)
# print(list1)




import tkinter
top = tkinter.Tk()
# 进入消息循环
top.mainloop()