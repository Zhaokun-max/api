import pytest
from selenium import webdriver
import time
# @pytest.fixture()
# def init():
#     print('初始化')
#     # 就是被测试的函数或者方法
#     yield
#     print('清理')
#
# def test_one(init):
#     print('测试步骤')

#

#使用selenuim 执行命令需要加上指定浏览器
#
@pytest.fixture()
def init(selenium):
    seleniu = webdriver.Chrome()
    #selenium.maximize_window()
    seleniu.implicitly_wait(30)
    seleniu.get('http://www.baidu.com/')
    yield
    selenium.quit()

def test_baidu_title(init,selenium):

    time.sleep(4)
    print(selenium.title)
    print(selenium.current_url)
    assert selenium.title == '百度一下，你就知道'

#     so=selenium.find_element_by_id('kw')
#     so.send_keys('pytest')
#     assert so.get_attribute('value')=='pytest'
#
