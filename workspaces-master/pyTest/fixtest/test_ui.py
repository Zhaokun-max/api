import pytest
from selenium import webdriver

# @pytest.fixture()
# def init():
#     print('初始化')
#     # 就是被测试的函数或者方法
#     yield
#     print('清理')
#
# def test_one(init):
#     print('测试步骤')

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    return driver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.baidu.com/")
driver.find_element_by_id('kw')

@pytest.fixture()
def init(driver):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://www.baidu.com/")
    yield
    driver.quit()

def test_baidu_title(init,driver):
    assert driver.title=='百度一下，你就知道'