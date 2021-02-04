import unittest
from selenium import webdriver


# 通过测试类的方式来执行一个类中的所有测试用例
class F7(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_001(self):
        pass
    def test_002(self):
        pass

if __name__ == '__main__':
#  测试类类中所有测试用例
#  加载测试类   按照模块执行
    suite=unittest.TestLoader().loadTestsFromTestCase(F7)
    unittest.TextTestRunner(verbosity=2).run(suite)
