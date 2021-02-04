#!/usr/bin/env python
#!coding:utf-8

def test_001():
    assert 1==1


def testadd():
    pass

class Testlogin(object):
    def test_loign_001(self):
        assert 1==1
    def test_loign_002(self):
        assert 1==1


def add(a,b):
    return a+b
#加入try会导致程序报错 用例执行错误也是成功的  也不要使用if或else
def test_add():
    try:
        assert add(1,'1')
    except Exception as e:
        print(e.args[0])
#-k
def test_smoke_001():
    assert 1==1

def test_smoke_002():
    assert 1==1


