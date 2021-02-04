import pytest
import requests

#conftest.py  共享  test_fix_conftest


def test_get_allbook(getToken):
    r=requests.get(
        url='http://127.0.0.1:5000/v1/api/books',headers={'Authorization':'JWT {0}'.format(getToken)}
    )
    print(r.json())
