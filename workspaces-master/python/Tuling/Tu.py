import time
from collections import namedtuple
# 循环遍历

metro_areas = [
    ('toy', 'jp', 36.3, (36.265542, 25.3412220)),
    ('delhi', 'in', 34.2, (37.26544,39.222233)),
    ('mex', 'mx', 20.142,(-10.266, -52.2664)),
    ('nuw', 'nu', 20.133, (-10.266, -1.365)),
    ('sao', 'br', 20.1566, (-10.2644, -10.656))
]
s = list(metro_areas)
for i in s:

    print(i)
for a, b, c, (k,v)in s:
    if v == -1.365:
        num  = int(input('请输入数字'))
        if num == 2:
            print('aini')

        else:
            print('wan')
    else:
        print('budeng')

print('{:5}| {:^9}| {:^9}'.format('', 'lat', 'long'))
sun = '{:5}| {:^9.4}|  {:^9.4}'
for name, cc, pop, (latl, longl) in metro_areas:
    if longl<=0:
        print(sun.format(name,latl,longl))

# 具名元组
#存放在对应字段里的数据要以一串参数的形式传入到构造函数中
# city = namedtuple('city', 'name country population coordinates ')
# # 生成一个city的实例对象
# tokyo = city('toy', 'jp', 36.3, (36.265542, 25.3412220))
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])
# pt = namedtuple('pt', ['name', 'age', 'self', 'pr'])
# toyo = pt('toy', 'jp', 36.3, (36.265542, 25.3412220))
# print(toyo)
# print(toyo.name)
# print(toyo[3])
# #属性是一个包含这个类所有字段名称的元组
# print(toyo._fields)







