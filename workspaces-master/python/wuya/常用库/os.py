import os

# 创建文件 mkdir
#os.mkdir("G:\log")
# 删除目录
#os.rmdir('G:\log')

# 改名字
#os.rename("G:\log",'G:\\newlog')

#对目录的处理
print('当前目录路径', os.path.dirname(__file__))
print('上一级目录', os.path.dirname(os.path.dirname(__file__)))

#实现对python下postman下A文件的读取

base_dir=os.path.dirname(os.path.dirname(__file__))
print(base_dir)
f=open(os.path.join(base_dir,'Postman/A.json'),'r')
print(f.read())

