from selenium import webdriver
import unittest
# 当浏览器无法获取当前页面网址，需要切换句柄实现，当前页面断言
class BaiDulink(unittest.TestCase):
    def setUp(self):
        self.drive=webdriver.Chrome()
        self.drive.get('https://www.baidu.com')
        #global h
        #h=self.drive.current_window_handle
        #print('首页句柄',h)
    def tearDown(self):
        self.drive.quit()

    def test_baidu_so_enable(self):
        '''首页：百度搜索输入框可编辑'''
        so=self.drive.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test_baidu_so(self):
        '''首页：百度搜索功能'''
        so=self.drive.find_element_by_id('kw')
        so.send_keys('webdriver')
        self.drive.find_element_by_id("su").click()

        #获取所有句柄  只有获取网址使用#  判断使用场景
        # all_h=self.drive.window_handles
        # #print('所有句柄',all_h)
        # #切换句柄，第几个标签页
        # self.drive.switch_to_window(all_h[1])
        # # #断言
        print(so.get_attribute('value'))
        self.assertEqual(so.get_attribute('value'),'webdriver')
if __name__ == '__main__':
    unittest.main(verbosity=2)