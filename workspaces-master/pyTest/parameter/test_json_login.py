import pytest
import requests
#from .operationJson import readJson
from pyTest.parameter.operationJson import readJson

@pytest.mark.parametrize('data',readJson())
def test_json_login(data):
    r=requests.post(url=data['request']['url'],
                    json=data['request']['url'])

    assert r.json()==data['response'][0]
if __name__ == '__main__':
    pytest.main(['-s','test_json_login.py'])