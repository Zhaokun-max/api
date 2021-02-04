import pytest



def add(a,b):
    return a+b

'''
参数化：是对列表中的对象煦暖，然后一一的赋值
对象：
列表，元组，字典

'''
#列表循环
# @pytest.mark.parametrize('a,b,expect',[
#                          [1,1,2],
#                          [2,2,4],
#                          [3,3,6],
#                          [4,4,8],
#                          [5,5,10]
# ])

#元组
# @pytest.mark.parametrize('a,b,expect',[
#     (1,1,2),
#     (2,2,4),
#     (3,3,6),
#     (4,4,8),
#     (5,5,10)
# ])
# def test_add(a,b,expect):
#     print(a,b,expect)
#     assert add(a,b)==expect

#字典

# @pytest.mark.parametrize('data',[
#     {"a":1,"b":1,"exccept":2},
#     {"a":2,"b":2,"exccept":4},
#     {"a":3,"b":3,"exccept":6},
#     {"a":4,"b":4,"exccept":8},
#     {"a":5,"b":5,"exccept":10},
# ])
# def test_add(data):
#     print(data)
#     assert add(data["a"],data["b"])==data["exccept"]
#
# if __name__ == '__main__':
#     pytest.main()


#标识
# @pytest.mark.parametrize('a,b,expect',
# [
#  pytest.param(1, 1, 2, id="pass"),
#  pytest.param(2, 2, 4, id="pass"),
#  pytest.param(3, 3, 6, id="pass"),
#  pytest.param(4, 4, 8, id="pass"),
#  pytest.param(5, 5, 10, id="pass"),
# ])
# def test_add(a,b,expect):
#     print(a,b,expect)
#     assert add(a,b)==expect
# 分离数据

data=[
    pytest.param(1,1,2,id="pass"),
    pytest.param(2,2,4,id="pass"),
    pytest.param(3,3,6,id="pass"),
    pytest.param(4,4,8,id="pass"),
    pytest.param(5,5,10,id="pass"),

]
@pytest.mark.parametrize('a,b,expect',data)
def test_two(a,b,expect):
    assert add(a,b)==expect