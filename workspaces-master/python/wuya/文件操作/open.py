'''
open函数的参数：
1.要操作的文件名称
2.以什么样的方式操作

r 只读模式
w 只写模式 不存在创建 存在清空赋值
x  只写模式 不存在就创建，存在报错
a：增加模式，可读 不存在创建，存在增加内容
+ 表示同时可以读写某个文件，具体位置
r+：读写
w+ 写读
x+ 写读
a+ 写读
'''

#f=open("w.json","w")
# temp={
#     "name":"panda",
#     "age":"18",
#     "adders":"ddd"
# }
# #f.writelines(temp)
# #f.close()
# import json
# json.dump(temp,open("w.json","w"))

'''
文件上下文处理
'''

with open("file","w") as f:
    f.write("panda\n")