"""
import random
import math

# num = input("情输入一个三位数")
    # 输入的字符类型 不转换则报错
    # 判断输入的数字，与系统随机数比较大小
    #
    # if num.isdigit() and 100 <= int(num) <= 999:
s = random.randrange(1,100)
print(s)
time = 3
while time:
    num = input("请输入数字")
    if num.isdigit():
        tmp = int(num)
        if tmp == s:
            print("panda")
            break
        elif tmp > s:
            print("woaini")
            time -= 1
        else:
            print("滚犊子")
            time -= 1
    else:
        print("请输入正确的正整数")
        time -= 1
print("结束")
"""

import random
import math
"""
输入一个三位数与程序随机数比较大小
如果程序大于程序随机数，则分别输出这个三位数的个位/十位/百位
如果等于程序随机数，则提示中奖，记100分
如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个字母，后8个是数字）
"""
class GameGum(object):
    #输入函数
    def line(self):
        str_num = ''
    # 定义一个空字符串用于拼接
        # 循环前四个随机字母用ascll对应的值来随机在转换为字母
        for i in range(4):
            # 随机小写ascll码
            num = random.randrange(97,123)
            # 将ascll值转换为字母
            str_s = chr(num)
            # 依次拼接得到的随机字母
            str_num = str_num + str_s
        # 循环后八个随机数字
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num + str(num)
        #print(str_num)
        return str_num


    def num_member(self, total, sourse):
        range_num = random.randrange(100, 1000)
        print(range_num)
        i = 1
        while True:

            num = input("请输入数字")
            if num == "1":
                break

            #程序随机数
            #检测输入是否为数字
            if num.isdigit() and 100 <= int(num) <= 999:# 输入函数返回的是字符串类型，不能与整性直接比对，需要转换
                total += 1
                print("输入有效次数为%d"%total)
                #sou = sourse//total
                #print("你中奖的概率为%{}".format(sou))
                num = int(num)
                range_num = int(range_num)
                if num >  range_num:

                    # 求百位数字方法是地板除 100或用数学模块 当中的floor()函数
                    bai = num//100
                    # 求十位数字方法是先把三位数字取100的余数，在地板除10
                    shi = num % 100 // 10
                    # 求各位数字方法是直接取10的模
                    ge = num % 10
                    print("你输入的数字比程序随机数大，随机数为{}".format(range_num))
                    print("这个三位数的百位是{}， 十位是{}， 个位是{}".format(bai, shi, ge))
                if num < range_num:
                    # 由于120个字符串每行12个可加只需存入10 行就可以
                    print("你输入的数字比程序随机数小，随机数为{}".format(range_num))
                    for i in range(10):
                        str_line = GameGum.line(self)
                        #print(str_line)
                        # 执行文件存入操作
                        with open('str_num.txt','a') as f:
                            f.write(str_line + "\n")
                            # with 自动关闭文件，open需加关闭操作
                            #f.close()
                if num == range_num:
                    sourse = sourse +100
                    sou = sourse // total
                    print("你中奖的概率为%{}".format(sou))
                    print("恭喜你中奖了目前分数为",sourse)
                    break
            else:
                if i == 3 :
                    print("请按规定输入")
                    break
                else:
                    print("请按规定输入")
                    i = i + 1
    # 程序入口
if __name__ == '__main__': # 调试代码
    # 在本身模块中__name__ == __main__ 当第三方导入的时候__name__ == 文件名
    # 下面调用函数
    sourse = 0
    # 定义一个变量用于累计输入次数
    total = 0
    #GameGum.num_member(0,total,sourse)
    #实例化类
    game =  GameGum()
    game.num_member(total,sourse)
    #通过类调用函数

