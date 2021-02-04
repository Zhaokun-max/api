import unittest

from unittesta.init import *

def add(a, b):
    return a - b

class baidulink(gujian):


    @unittest.skip('该功能取消忽略测试用例的执行')
    def test_baidu_news(self):
        self.drive.find_element_by_link_text('新闻').click()

    def test_baidu_002(self):
        self.drive.find_element_by_link_text('地图').click()

    # 期望访问失败
    @unittest.expectedFailure
    def test_baidu_003(self):
        self.assertEqual(add(2-3),1)
if __name__ == '__main__':
# 分离测试套件

    unittest.main(verbosity=2)
