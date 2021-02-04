import random
import unittest

class TestSer(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        print(self.seq)
    def tearDown(self):
        pass

    def test_choice(self):
        #从序列seq中随机选取一个元素
        element=random.choice(self.seq)
        print(element)
        #验证随机元素确实属于列表中
        self.assertTrue(element in self.seq)

    def test_sample(self):
        #验证执行的语句是否抛出了异常
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue((element in self.seq))


class TestDICT(unittest.TestCase):
    def setUp(self):
        # 创建整数列表（导致“TypeError: ‘range’ object
        # does
        # not support
        # item
        # assignment”）有时你想要得到一个有序的整数列表，所以range()
        # 看上去是生成此列表的不错方式。然而，你需要记住range()
        # 返回的是“range
        # object”，而不是实际的list
        # 值。
        self.seq= list(range(10))

    def tearDown(self):
        pass

    def test_shuffle(self):
        #随机打乱元seq的顺序
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        #验证执行函数时抛出了TypeERROR异常
        self.assertRaises(TypeError, random.shuffle,(1,2,3))


if __name__ == '__main__':
    #根据给定的测试类，获取其中的所有已test开头的测试方法，并返回一个测试套件
    testcase1=unittest.TestLoader().loadTestsFromTestCase(TestSer)
    testcase2=unittest.TestLoader().loadTestsFromTestCase(TestDICT)
    #将多个测试类加载到测试套件中
    suite=unittest.TestSuite(testcase1,testcase2)
    #设置执行详细信息
    unittest.TextTestRunner(verbosity=2).run(suite)
