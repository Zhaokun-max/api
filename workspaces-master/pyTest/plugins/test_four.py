
import pytest
import requests

def test_taobao_001():
    r =requests.get(
        url='http://www.taobao.com'
    )
    assert r.status_code==200

# def test_baidu_001():
#     r=requests.get(
#         url='http://www.baidu.com',
#         timeout=0.01
#     )
#     assert r.status_code == 200

@pytest.mark.smoke
def test_001():
    assert 1==1