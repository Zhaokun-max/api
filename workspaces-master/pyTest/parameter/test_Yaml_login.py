import requests
import pytest
#反序列化处理
import json
from .operationYaml import readYaml

@pytest.mark.parametrize('data',readYaml())
def test_login(data):
    r=requests.post(
        url=data['url'],
        json=json.loads(data['body'])
    )
    assert r.json()==json.loads(data['except'])

