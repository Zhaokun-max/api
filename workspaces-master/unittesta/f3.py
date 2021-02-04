
#:/usr/bin/evn python
#-*-coding:utf-8-*-


import unittest
from selenium import webdriver
import time

class F2(unittest.TestCase):

    def setUp(self):
        self.drive=webdriver.Chrome()
        self.drive.maximize_window()
        self.drive.implicitly_wait(30)
        self.drive.get('https://www.baidu.com/')

    def tearDown(self):
        self.drive.quit()
# 执行顺序按照ascll码进行执行  ord
    def test_baidu_news(self):
        self.drive.find_element_by_link_text('新闻').click()
        time.sleep(5)
    def test_baidu_map(self):
        self.drive.find_element_by_partial_link_text('地图').click()

if __name__ == '__main__':
    unittest.main(verbosity=2)