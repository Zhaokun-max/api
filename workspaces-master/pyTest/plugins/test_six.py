

import pytest


@pytest.mark.dependency()
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    assert True

#测试C依赖于测试A
@pytest.mark.dependency(depends=['test_a'])
def test_c():
    pass

#测试d依赖于测试b
@pytest.mark.dependency(depends=['test_b'])
def test_d():
    pass