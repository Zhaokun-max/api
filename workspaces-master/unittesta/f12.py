import unittest
from unittesta.init import *
class baidulink(gujian):
# 断言
     # 判断是否相等   #扩展其他断言
#     def test_baidu_news(self):
#         self.assertEqual(self.drive.title,'百度一下，你就知道')
#
    def test_baidu_sosuo(self):
        so=self.drive.find_element_by_id('kw')
        print(so.is_enabled())
        #判断是否编辑，结果是不是True，是的话OK
        self.assertTrue(so.is_enabled())

        # # 判断是fou编辑，结果是false 报错
        # self.assertFalse(so.is_enabled())
   # 判断值是否在title中
    def test_baidu_title(self):
        self.assertIn('百度',self.drive.title)

if __name__ == '__main__':
# 分离测试套件
    unittest.main(verbosity=2)


#断言注意事项
