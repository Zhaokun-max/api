from selenium import webdriver
import unittest
import time
# 当浏览器无法获取当前页面网址，需要切换句柄实现，当前页面断言
class BaiDulink(unittest.TestCase):
    def setUp(self):
        self.drive=webdriver.Firefox()
        self.drive.get('https://www.baidu.com')
        global h
        h=self.drive.current_window_handle
        #print('首页句柄',h)
    def tearDown(self):
        self.drive.quit()
    def test_baidu_news(self):
        '''点击首页新闻是否正常跳转'''
        self.drive.find_element_by_partial_link_text('新闻').click()
        #获取所有句柄
        all_h=self.drive.window_handles
        #print('所有句柄',all_h)
        #切换句柄，第几个标签页
        self.drive.switch_to_window(all_h[1])
        #断言
        self.assertEqual(self.drive.current_url,'http://news.baidu.com/')
        #print(self.drive.current_url)
        #关闭新窗口
        #self.drive.close()
        #切换到首页句柄
        #self.drive.switch_to_window(h)
        #打印当前title
        #print(self.drive.title)
        #self.assertEqual(self.drive.title,'百度一下，你就知道')
    # def test_baidu_map(self):
    #     '''测试百度地图'''
    #     self.drive.find_element_by_link_text('地图').click()
    #     time.sleep(5)
    #     self.assertEqual(self.drive.current_url,'https://map.baidu.com/@12959238.56,4825347.47,12z')

if __name__ == '__main__':
    unittest.main(verbosity=2)