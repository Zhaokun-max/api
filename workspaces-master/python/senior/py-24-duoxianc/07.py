import time
import threading

def fun():
    print("Start at:",time.ctime())
    time.sleep(2)
    print("end time",time.ctime())

print("main thread")

t1 = threading.Thread(target=fun,args=())
t1.setDaemon(True)
t1.start()
#和商面daemon一致
#t1.daemon=True
time.sleep(1)
print("game over")