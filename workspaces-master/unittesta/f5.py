#:/usr/bin/evn python
#-*-coding:utf-8-*-


import unittest
from selenium import webdriver

class Baidutest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.drive=webdriver.Chrome()
        cls.drive.maximize_window()
        cls.drive.implicitly_wait(50)
        cls.drive.get('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.drive.quit()

    def test_baidu_news(self):
        self.drive.find_element_by_link_text('新闻').click()
        self.drive.close()

    def test_baidu_map(self):
        self.drive.find_element_by_partial_link_text('图').click()
        self.drive.close()


if __name__ == '__main__':
    #初始化处理
    suite=unittest.TestSuite()
    #调用类方法
    suite.addTest(Baidutest('test_baidu_nwes'))
    suite.addTest(Baidutest('test_baidu_map'))
    unittest.TextTestRunner(verbosity=2).run(suite)