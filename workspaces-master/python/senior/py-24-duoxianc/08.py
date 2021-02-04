import time
import threading


def loop1(in1):
    # ctime得到当前时间
    try:
        print('Start loop l at:',time.ctime())
        # 把参数打印
        print("我是参数",in1)
        #睡眠时间，单位秒
        time.sleep(10)
        print('End loop l at:',time.ctime())
    except:
        print("eeeeee")

def loop2(in1,in2):
    # ctime得到当前时间
    try:
        print('Start loop 2 at:',time.ctime())
        # 把参数打印
        print("我是参数",in1,"和参数",in2)
        #睡眠时间，单位秒
        time.sleep(2)
        print('End loop 2 at:',time.ctime())
    except:
        print("eeeeee")

def loop3(in1,in2):
    # ctime得到当前时间
    try:
        print('Start loop 2 at:',time.ctime())
        # 把参数打印
        print("我是参数",in1,"和参数",in2)
        #睡眠时间，单位秒
        time.sleep(10)
        print('End loop 2 at:',time.ctime())
    except:
        print("eeeeee")
def mian():
    print("Start at:",time.ctime())

    t1 = threading.Thread(target=loop1, args=("panda",))
    t1.start()
    t1.setName("TH1-1")

    t2 = threading.Thread(target=loop2, args=("盼达","zeilin"))
    t2.start()
    t2.setName("TH2-2")

    t3 = threading.Thread(target=loop3, args=("盼达","zeilin"))
    t3.start()
    t3.setName("TH3-3")

#   预期3秒后thread2已经结束
    time.sleep(5)
#enumerate 得到正在运行的子线程
    for thr in threading.enumerate():
        # getname能够得到线程的名字
        print(' 正在运行线程的名字是：{}'.format(thr.getName()))
        print("正在运行的线程数量为:{}".format(threading.activeCount()))
        print("ALL DONE AT",time.ctime())


if __name__ == '__main__':
    mian()

    while True:
        time.sleep(1)