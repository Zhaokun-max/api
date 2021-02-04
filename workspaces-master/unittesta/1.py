# #:/usr/bin/evn python
# #-*-coding:utf-8-*-
#
#
import unittest

class F1(unittest.TestCase):
    #准备工作  限制性serup在执行 test-001在执行teardown
    def setUp(self):
        print('我已经做好了准备工作')
    # 结束运行
    def tearDown(self):
        print('已经处理')
    # 开始处理test测试用例
    def test_001(self):
        #admin
        print('admin')
    def test_002(self):
        print('test')
    def test_003(self):
        print('test')


if __name__ == '__main__':

    # 单独执行不需要加容器suite，main执行单独
    unittest.main(verbosity=0)

# verbosity  不填写默认为1   得到详细的信息
# verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
# 0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
# 1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
# 2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
