import unittest
import os
import HTMLTestRunner
import time
def alltests():
    suite=unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None)
    return suite

def getNowTime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    fp=os.path.join(os.path.dirname(__file__), 'report',getNowTime()+'testReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp,'wb'),
        title='自动化测试报告',
        description='自动化测试报告详细信息').run(alltests())

if __name__ == '__main__':
    run()


# 目的生成代码统计率
#命令行 cd进入脚本目录  coverage run all...py文件执行
# 接着执行 coverage html 统计代码覆盖率
#拼接目录    在report目录下写入  html文件
#print(os.path.join(os.path.dirname(__file__),'report','testReport.html'))
#查看调用的测试用例
#print(alltests())

#查看目录
#print(os.path.dirname(__file__))