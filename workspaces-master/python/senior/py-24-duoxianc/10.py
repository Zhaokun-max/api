from time import sleep, ctime
import threading
loop = [4,2]

class ThreadFunc:

    def __init__(self, name):
        super(ThreadFunc, self).__init__()
        self.name=name

    def loop(self, nloop, nsec):

        # param nloop：loop函数的名称
        # param nsec：系统西米那时间
        # return：
        print("Start loop", nloop, "at", ctime())
        sleep(nsec)
        print("Done loop", nloop, "at", ctime())

def main():

    print("Strat at:", ctime())
    # ThreadFunc("loop").loop 跟以下两个狮子相等
    # t = ThreadFunc("loop")
    # t.loop
    # 一下t1和t2的定义方式相等
    t = ThreadFunc("loop")
    t1 = threading.Thread(target = t.loop, args=("loop1", 4))
    t2 = threading.Thread(target = ThreadFunc("loop".loop, args=("loop2",2)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ALL_DONE_AT:", ctime())


if __name__ == '__main__':

    main()