#参数化
import pytest

def add(a,b):
    return a+b

# @pytest.fixture(params=[
#     [1,1,2],
#     [2,2,4],
#     [3,3,6]
# ])
# def getDate(request):
#     return request.param
#
# def test_one(getDate):
#     #列表下标索引
#     assert add(getDate[0],getDate[1])==getDate[2]
#

datas=[
    [1,1,2],
    [2,2,4],
    [3,3,6]
]
#参数化用这种方式
@pytest.fixture(params=datas)
def getDate(request):
    return request.param

def test_one(getDate):
    #列表下标索引
    assert add(getDate[0],getDate[1])==getDate[2]