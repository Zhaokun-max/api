#:/usr/bin/evn python
#-*-coding:utf-8-*-



import unittest
from selenium import webdriver
import time

# class test_lonin(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.drive=webdriver.Chrome()
#         #cls.drive.maximize_window()
#         cls.drive.implicitly_wait(3)
#         cls.drive.get('http://test.portal.jlncjy.cacfintech.com')
#
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.drive.quit()



#请编写python代码操作字符串：the_str='12,33,44'
the_str='12,33,44'
add=the_str.split(',')
cc=''.join(add)
print(cc)

