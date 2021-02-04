import requests
import pytest

def test_baidu():
    r=requests.get(url='http://www.baidu.com')
    assert r.status_code==200
def test_taobao():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200
def test_jd():
    r=requests.get(url='http://www.jd.com')
    assert r.status_code == 200
def test_sina():
    r=requests.get(url='http://www.sina.com')
    assert r.status_code == 200

def test_taobao1():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200


def test_taobao2():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200

def test_taobao3():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200


def test_taobao4():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200


def test_taobao5():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200


def test_taobao6():
    r=requests.get(url='http://www.taobao.com')
    #查看响应时间
    print(r.elapsed.total_seconds())
    assert r.status_code==200

