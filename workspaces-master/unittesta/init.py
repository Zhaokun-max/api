import unittest
from selenium import webdriver

class gujian(unittest.TestCase):

    def setUp(self):
        self.drive = webdriver.Chrome()
        self.drive.maximize_window()
        self.drive.implicitly_wait(30)
        self.drive.get('http://www.baidu.com')

    def tearDown(self):
        self.drive.quit()