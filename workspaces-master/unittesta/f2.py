    #:/usr/bin/evn python
    #-*-coding:utf-8-*-


import unittest
from selenium import webdriver

class F2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drive=webdriver.Chrome  ()
        cls.drive.maximize_window()
        cls.drive.implicitly_wait(50)
        cls.drive.get('http://baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.drive.quit()

    def test_baidu_news(self):
        self.drive.find_element_by_link_text('新闻').click()
        self.drive.back()

    def test_baidu_map(self):
        self.drive.find_element_by_partial_link_text('图').click()
        self.drive.back()

    def test_baidu_mbp(self):
        self.drive.find_element_by_partial_link_text('地图').click()
        self.drive.back()

if __name__ == '__main__':
    unittest.main()