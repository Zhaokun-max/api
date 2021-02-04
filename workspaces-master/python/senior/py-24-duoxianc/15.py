import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def fun_c():
    print("fun_1 start")
    lock_1.acquire(timeout=4)
    print("func_1 申请了 lock_1")
    time.sleep(2)
    print("func_1 等待 lock_2")

    rst = lock_2.acquire(timeout=1)
    if rst:
        print("fun_1已经得到锁lock_2")
        lock_2.release()
        print("fun_1释放lock_2")
    else:
        print("fun_1 注定没有申请到lock_2")

    lock_1.release()
    print("fun_1 释放了 lock_1")

    print("done")

def fun_2():
    print("fun_2 start")
    lock_2.acquire()
    print("func_2 申请了 lock_2")
    time.sleep(4)
    print("func_2 等待 lock_1")
    lock_1.acquire()
    print("fun_2申请lock_1")
    lock_1.release()

    print("fun_2 释放了 lock_1")

    lock_2.release()

    print("fun_2释放了lock_2")

    print("done")

if __name__ == '__main__':
    print("主程序启动")

    t1 = threading.Thread(target=fun_c, args=())
    t2 = threading.Thread(target=fun_2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()