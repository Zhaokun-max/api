import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml
import json
obj=Requests()
objYaml=OperationYaml()

@pytest.mark.parametrize('datas',objYaml.readYaml())
def test_login(datas):

    r=obj.post(url=datas['url'],
               json=datas['data'])
    #如果返回的编码是乱码经过一下处理，处理后是字符串
    #print(json.dumps(r.json(),ensure_ascii=False))
    assert datas['expect'] in json.dumps(r.json(),ensure_ascii=False)
    print(r.json())

if __name__ == '__main__':
    pytest.main(['-v','-s','test_login.py'])