'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
def loop1():
    # ctime得到当前时间
    print('Start loop l at:',time.ctime())
    #睡眠时间，单位秒
    time.sleep(4)
    print('End loop l at:',time.ctime())

def loop2():
    # ctime得到当前时间
    print('Start loop 2 at:',time.ctime())
    #睡眠时间，单位秒
    time.sleep(6)
    print('End loop 2 at:',time.ctime())

def mian():
    print('String at:',time.ctime())
    loop1()
    loop2()
    print('All done at:',time.ctime())


if __name__ == "__main__":
    mian()