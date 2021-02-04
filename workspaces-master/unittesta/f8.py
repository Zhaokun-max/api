from selenium import webdriver
import unittest


class baidulink(unittest.TestCase):

    def setUp(self):
        self.drive=webdriver.Firefox()
        self.drive.maximize_window()
        self.drive.implicitly_wait(30)
        self.drive.get('http://www.baidu.com')
    def tearDown(self):
        self.drive.quit()
    def test_baidu_news(self):
        self.drive.find_element_by_link_text('新闻').click()
    def test_baidu_map(self):
        self.drive.find_element_by_partial_link_text('地图').click()

class baiduso(unittest.TestCase):

    def setUp(self):
        self.drive=webdriver.Firefox()
        self.drive.maximize_window()
        self.drive.implicitly_wait(30)
        self.drive.get('http://www.baidu.com')
    def tearDown(self):
        self.drive.quit()
    def test_so(self):
        self.drive.find_element_by_id('kw').send_keys('webdrive')

if __name__ == '__main__':
    # 测试百度搜索 不执行baidulink   按模块执行    module加载测试模块
    # 按照测试类执行
    suite=unittest.TestLoader().loadTestsFromModule('f8.py')
    unittest.TextTestRunner(verbosity=2).run(suite)

