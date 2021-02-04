import pytest
import requests
#  跳过测试与预期失败的测试
@pytest.mark.skip(reason='跳过用例执行')
def test_iphon_001():
    assert 1==1

@pytest.mark.skip(reason='跳过用例执行')
def test_iphon_002():
    assert 1 == 1


def test_login_001():
    assert 1 == 1


def test_login_002():
    assert 1 == 1
#标记为失败用例
@pytest.mark.xfail(reason='期望返回的状态码是200，实际是406')
def test_chanquan_001():
    deic = {
        "password": "123456",
        "username": "18812"
    }
    r=requests.post(url='http://test.admin.jlncjy.cacfintech.com/api/v1.0/chanquan/user/login',
                    json=deic)
    #print(r.status_code)
    assert r.status_code==200


