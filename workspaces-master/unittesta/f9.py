import unittest

from unittesta.init import *
# 通过测试类的方式来执行一个类中的所有测试用例
class baidulink(gujian):

    def test_baidu_news(self):
        self.drive.find_element_by_link_text('新闻').click()

    def test_baidu_002(self):
        self.drive.find_element_by_link_text('地图').click()
    @staticmethod  #静态方法
    def suite(self):
        # 加载测试套件
        suite = unittest.TestSuite(unittest.makeSuite(baidulink))
        return suite


if __name__ == '__main__':
# 分离测试套件

    unittest.TextTestRunner(verbosity=2).run(baidulink.suite())
