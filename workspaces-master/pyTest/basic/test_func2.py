import pytest
import unittest
def test_001():
    assert 1==1


class TestLogin(object):
    def test_login(self):
        assert 1==1

class Longin(unittest.TestCase):

    def test_003(self):
        pass

#执行使用pytest -v test_func1.py
