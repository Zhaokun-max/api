#打印字母A
#控制行
class Game():
    def a(self):
        for i in range(1,5):
            # 判断开始输入的位置
            for k in range(5-i):
                print("",end = " ")
            #控制列
            for j in range(1, i + 1):
                if i == 1 or i == 3 or j ==1 or j == i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    # 打印字母B
    def b(self):
        for i in range(1,4):
            for j in range(1,4):
                if i == 1 or i == 4 or j ==1:
                    if j < 3:
                        print("*",end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print("*",end = " ")
                else:
                    print(" ",end = " ")
            print()
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印字母C
    def c(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i ==4:
                    if j == 1:
                        print("",end="")
                    else:
                        print("*",end="")
                elif j == 1:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print("",end=" ")

                print(" ",end=" ")
            print()
    #打印字母D
    def d(self):
        for i in range(1, 5):
            for j in range(1, 4):
                if i == 1 or i == 4 or j == 1:
                    if j < 3:
                        print("*", end=" ")
                elif j == 3:
                    if i == 2 or i == 3:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    # 打印字母E
    def e(self):
        for i in range(1,8):
            for j in range(1,5):
                if i == 1 or i == 4 or i ==7 or j == 1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    # 打印F
    def f(self):
        for i in range(1,6):
            for j in range(1,5):
               if i == 1 or i == 3 or j == 1:
                   print("*",end=" ")
               else:
                   print(" ",end="")
            print()
    # 打印G
    def g(self):
        for i in range(1,6):
            for j in range(1,6):
               if i == 1 or i ==5:
                   if j == 1:
                       print(" ", end=" ")
                   else:
                       print("*",end=" ")
               elif i == 1 or j == 1:
                   print("*",end=" ")
               elif i == 4:
                   if j == 2:
                    print(" ",end=" ")
                   else:
                    print("*",end=" ")
            else:
                print("",end=" ")
            print()
    # 打印H
    def h(self):
        for i in range(1,6):
            for j in range(1,5):
                if j ==1 or j == 4 or i == 3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    # 打印I
    def i(self):
        for i in range(1,6):
            for j in range(1,6):
                if i == 1 or i == 5 or j == 3:
                    print("*",end= ' ')
                else:
                    print(" ",end=" ")
            print()
    # 打印J
    def j(self):
        for i in range(1,6):
            for j in range(1,6):
                if i == 1 or j == 4:
                    if i < 5:
                        print("*",end=" ")
                elif i == 4 and j == 1:
                    print("*",end=" ")
                elif i == 5 and j == 2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    # 打印K
    def k(self):
        for i in range(1,3):
            for j in range(i ,4):
                if i == 1  and j ==2:
                    print(" ",end=" ")
                else:
                    print("*",end=" ")
            print()
        for i in range(1,4):
            for j in range(i):
                if i == 3 and j == 1:
                    print(" ",end=" ")
                else:
                    print("*",end=" ")
            print()
    # 打印L
    def l(self):
        for  i in range(1,5):
            for j in range(1,4):
                if i == 4 or j ==1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    # 打印M
    def m(self):
        for i in range(1,5):
            # 判断开始输入的位置
            for k in range(5-i):
                print("",end = " ")
            #控制列
            for j in range(1, i + 1):
                if i == 1 or j ==1 or j == i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            # 判断开始输入的位置
            for k in range(5-i):
                print("",end = "  ")
            #控制列
            for j in range(1, i + 1):
                if i == 1 or j ==1 or j == i:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #打印N
    def n(self):
        for m in range(1,5):
            for n in range(1,5):
                if n == 4 or n ==1 or m==n:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    # 打印O
    def o(self):
        for m in range(1,5):
            for n in range(1,5):
                if m == 2 or m == 3 or n == 2 or n ==3 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()