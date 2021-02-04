import unittest

##当前目录
test_dir='./'
#找到测试用例方法
discovery = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':

    runner = unittest.TextTestRunner()

    runner.run(discovery)