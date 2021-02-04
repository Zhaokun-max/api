import threading
import time

# 参数定义最多几个线程同时使用资源
semphore = threading.Semaphore(3)

def func():
    if semphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + "   get semphore")
        time.sleep(5)
        semphore.release()
        print(threading.currentThread().getName() + "   release semphore")

for i in range(8):
    t1 = threading.Thread(target=func, args=())
    t1.start()