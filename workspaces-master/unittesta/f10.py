
from unittesta.init import *
# 分离测试固件
class baiduso(gujian):

    def test_so(self):
        self.drive.find_element_by_id('kw').send_keys('webdrive')

if __name__ == '__main__':
    unittest.main(verbosity=2)