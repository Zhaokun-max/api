
# 被测试类

class Math:
    # 构造方法获得a和b的值
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

# 加法计算方法
    def add(self):
        return self.a + self.b

# 减法计算方法
    def sub(self):
        return self.a-self.b

