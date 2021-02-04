#:/usr/bin/evn python
#-*-coding:utf-8-*-


import unittest
from selenium import webdriver

class F6(unittest.TestCase):

    def test_user_001(self):
        '''添加用户'''
        print('add')

    def test_user_002(self):
        '''删除用户'''
        print('del')


if __name__ == '__main__':
    # 按照测试类执行   类是F6，有其他类放其他类
    suite=unittest.TestSuite()
    suite.addTest(F6)
    unittest.TextTestRunner(verbosity=2).run(suite)

