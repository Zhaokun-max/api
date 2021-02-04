import random
# 定义一个变量用于存取初始分数
sourse = 0
while 1:
    num = input("输入数字")
    if num == 1:
        break
    rand_num = random.randrange(1,4)
    print(rand_num)
    num = int(num)

    rand_num = int(rand_num)
    if num > rand_num:
        print("输入的数字比随机数大{}".format(rand_num))
    elif num < rand_num:
        sourse += 100
        print("太棒了 分数为{}".format(sourse))

    else:
        print("输入的数字比随机数小{}".format(rand_num))
    if num == 2:
        break