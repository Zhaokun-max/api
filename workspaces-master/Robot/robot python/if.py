# 列出1-10数字所有的平方
#第一种
# l=[]
# for i in range(1,11):
#     l.append(i**2)
# print(l)
#
# #列出1-10中大于等于4的数字的平方,普通方法
# l = []
# for i in range(1,11):
#     if i>=4:
#         l.append(i**2)
# print(l)
#
# # 解析方法
# l=[i**2 for i in range(1,11) if i>=4]
# print(l)
#
# #嵌套循环。实现两个列表中的元素逐一配对
#
# a=["a","b","c"]
# b=[1,2,3]
# c=[]
# for k in a:
#     for v in b:
#         c.append((k,v))
# print(c)
#
# #列表解析
# l3=[(k,v) for k in a for v in b]
# print(l3)
#
# 集合解析，提取 单词序列中每个单词的首字母，创建一个集合set
# words=["ad","cd"]
# first=set()
# for w in words:
#     first.add(w[0])
#     print(first)
# # 代码可修改为
# first={ w[0] for w in words }
# print(first)

# 字典解析
#将原有的字段的键和值互换，从而创建一个新的字典
org={'a':1,"b":2}
filppend={}
for key,values in org.items():
    filppend[values]=key
print(filppend)

#同样代码改写
filppend={values:key for key,values in org.items()}
print(filppend)

