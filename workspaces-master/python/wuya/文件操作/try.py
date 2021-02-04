



#异常

# def div(a,b):
#     return a/b
# try:
#
#     div(1, 'i')
# except ZeroDivisionError as e:
#     print(e.args)
# except Exception as e:
#     print('输入格式错误,请重新输入')


'''
1.try--->exception-->else--->finally
2.先执行try，如果执行通过，就执行else代码，最后执行finally
3.如果try执行失败，就直接执行finally
'''
def di(a,b):
    return a/b

try:
    di(1,"s")
except Exception as f:
    print("EX")
else:
    print("else")
finally:
    print("finally")