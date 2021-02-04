import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿


class VerificationCode:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.find_element = self.driver.find_element_by_xpath

    def get_pictures(self):
        self.driver.get('http://test.portal.jlncjy.cacfintech.com/')  # 打开登陆页面
        time.sleep(5)
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        img = self.find_element('//*[@id="app"]/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[4]/div/img')  # 验证码元素位置
        time.sleep(1)
        location = img.location
        size = img.size  # 获取验证码的大小参数
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        image_obj.show()  # 打开切割后的完整验证码
        self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj

    def processing_image(self):
        image_obj = self.get_pictures()  # 获取验证码
        img = image_obj.convert("L")  # 转灰度
        pixdata = img.load()
        w, h = img.size
        threshold = 160
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        return img

    def delete_spot(self):
        images = self.processing_image()
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        images.show()
        return images

    def image_str(self):
        image = self.delete_spot()
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        result = pytesseract.image_to_string(image)  # 图片转文字
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        result_four = resultj[0:4]  # 只获取前4个字符
        print(resultj) # 打印识别的验证码
        return result_four
'''
def test_login_001(self):
        另一种获取图片验证码方式
        #self.drive.find_element_by_xpath("//*[@id='app']/div[3]/div[1]/div/div").click()
        self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[1]/div/div/label[2]/span[1]/span").click()
        username=self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[2]/div/div/input")
        password=self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[3]/div/div/input")
        #验证图片验证码元素
        code1=self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[3]/form/div[4]/div/div/input")
        # #截图到目录下
        time.sleep(2)
        self.drive.save_screenshot("G://test/01.png")
        #获取屏幕内容，截取保存验证码
        ran=Image.open("G://test/01.png")
        # 获取验证码位置，手动定位代表（左，上，右，下）
        box = (1040, 630, 1138, 667)
        ran.crop(box).save("G://test/02.png")
        #获取验证码图片，读取验证码
        imageCode = Image.open("G://test/02.png")  # 图像增强，二值化
        imageCode.load()
        imageCode.show()
        sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
        sharp_img.save("G://test/03.png")
        sharp_img.load()  # 对比度增强
        print(sharp_img)
        time.sleep(2)
        code = pytesseract.image_to_string(sharp_img).strip()
        #收到验证码，进行输入验证
        print(code)
        time.sleep(10)
        username.send_keys("18701079606")
        password.send_keys("020011")
        code1.send_keys(code)
        self.drive.find_element_by_xpath(".//*[@id='app']/div[3]/div[2]/div/div[2]/div/div/div[4]/p").click()
        '''
if __name__ == '__main__':
    a = VerificationCode()
    a.image_str()