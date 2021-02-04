#fixture重命名
'''
function  函数
class  类
module  模块
session  会话

'''
import pytest
#函数级别 class 重命名为a  为了简化函数名称
@pytest.fixture(scope='class',name='a')
def getNum():
    return 32

def test_num(a):
    assert a==32