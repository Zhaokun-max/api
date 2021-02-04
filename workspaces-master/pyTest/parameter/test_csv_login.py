import requests
import pytest
#反序列化处理
import json
from .operationCsv import readCsv

@pytest.mark.parametrize('data',readCsv())
def test_login(data):
    # print(data[0])
    # print(type(data[0]))
    r=requests.post(
        url=data[0],
        json=json.loads(data[1])
    )
    assert r.json()==json.loads(data[2])

