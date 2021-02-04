import time
import threading

def fun():
    print("Start at:",time.ctime())
    time.sleep(2)
    print("end time",time.ctime())

print("main thread")

t1 = threading.Thread(target=fun,args=())
t1.start()
time.sleep(1)
print("game over")