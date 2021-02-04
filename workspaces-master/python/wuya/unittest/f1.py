#:/usr/bin/evn python
#-*-coding:utf-8-*-


import unittest

class F1(unittest.TestCase):
    #准备工作  限制性serup在执行 test-001在执行teardown
    def setUp(self):
        print('我已经做好了准备工作')
    # 结束运行
    def tearDown(self):
        print('已经处理')
    # 开始处理test测试用例
    def test_001(self):    #
        print('admin')
    def test_002(self):
        print('test')
    def test_003(self):
        print('test')

if __name__ == '__main__':
    unittest.main(verbosity=2)
