#:/usr/bin/evn python
#-*-coding:utf-8-*-

from por.init import test_lonin
import unittest
from PIL import Image,ImageEnhance
import pytesseract
import time

class portal_fabu_001(test_lonin):
    def test_login_001(self):
        '''登录'''
        #self.drive.find_element_by_xpath("//*[@id='app']/div[3]/div[1]/div/div").click()
        self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[1]/div/div/label[2]/span[1]/span").click()
        username=self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[2]/div/div/input")
        password=self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[3]/div/div/input")
        # #验证图片验证码元素
        # code1=self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[4]/div/div/input")
        # # #截图到目录下
        # time.sleep(2)
        # self.drive.save_screenshot("G://test/01.png")
        # #获取屏幕内容，截取保存验证码
        # ran=Image.open("G://test/01.png")
        # # 获取验证码位置，手动定位代表（左，上，右，下）
        # box = (1040, 630, 1138, 667)
        # ran.crop(box).save("G://test/02.png")
        # #获取验证码图片，读取验证码
        # imageCode = Image.open("G://test/02.png")  # 图像增强，二值化
        # imageCode.load()
        # imageCode.show()
        # sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
        # sharp_img.save("G://test/03.png")
        # sharp_img.load()  # 对比度增强
        # print(sharp_img)
        # time.sleep(2)
        # code = pytesseract.image_to_string(sharp_img).strip()
        # #收到验证码，进行输入验证
        # print(code)
        # time.sleep(10)
        username.send_keys("18701079606")
        password.send_keys("020011")
        time.sleep(4)
        #code1.send_keys(code)
        self.drive.find_element_by_xpath("//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[4]/p").click()
        time.sleep(4)
        self.assertIn('http://test.portal.jlncjy.cacfintech.com/#/index',self.drive.current_url)

    def test_fabu_001(self):
        '''流转发布第一步'''
        '''断言是否在第一页面'''
        #点击发布按钮
        self.drive.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/p[1]').click()
        #断言
        self.assertIn('http://test.portal.jlncjy.cacfintech.com/#/publish-project/publisher-info',self.drive.current_url)
        # 滚动至元素ele可见位置
        eles = self.drive.find_element_by_xpath('//*[@id="app"]/div[4]/div/section/div/form/div[7]/p')
        ele = eles[0]
        driver.execute_script("arguments[0].scrollIntoView();", ele)
        self.drive.find_element_by_xpath('//*[@id="app"]/div[4]/div/section/div/form/div[7]/p').click()


        # 获取某个元素的文本信息.text
        message = driver.find_element_by_id(".//*[@id='app']/div[4]/div/section/div/form/div[1]/div[1]/div/div/input").text
        # 判断如果有这个文本信息，那么布尔值是真的，否则就是假的
        if (message.startswith("郑志钰!")):
            print("登录成功")
        else:
            print("登录失败")
#
if __name__ == '__main__':
    unittest.main(verbosity=2)