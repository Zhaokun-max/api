# -m  分组执行
import pytest


# -x失败后立即停止，并把失败的实测用例

def test_002():
    assert 1==2

@pytest.mark.smoke
def test_smoke_001():
    assert 1==1
# 调用py文件，执行所有函数，包括装饰器内函数   装饰器为分组指型
@pytest.mark.smoke
def test_smoke_002():
    assert 1==1

@pytest.mark.login
def test_login_002():
    assert 1==1

@pytest.mark.smoke
@pytest.mark.login
def test_login_003():
    assert 1==1

