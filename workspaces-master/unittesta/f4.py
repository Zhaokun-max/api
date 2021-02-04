
#:/usr/bin/evn python
#-*-coding:utf-8-*-


import unittest
from selenium import webdriver

class F2(unittest.TestCase):

    def setUp(self):

        self.drive=webdriver.Chrome()
        self.drive.maximize_window()
        self.drive.implicitly_wait(30)
        self.drive.get('https://www.baidu.com/')

    def tearDown(self):
        self.drive.quit()
# 执行顺序按照ascll码进行执行  ord
    '''百度首页的测试'''
    def test_baidu_001(self):
        '''百度首页测试：验证新闻的链接'''
        self.drive.find_element_by_link_text('新闻').click()

    def test_baidu_002(self):
        '''百度首页测试：验证地图的链接'''
        #捕获关键字
        self.drive.find_element_by_partial_link_text('图').click()

    '''百度搜索的测试'''
    def test_baidu_003(self):
        '''首页链接测试：验证搜索的链接'''
        #捕获关键字
        self.drive.find_element_by_id('kw').send_keys('webdrive')

if __name__ == '__main__':
    unittest.main(verbosity=2)