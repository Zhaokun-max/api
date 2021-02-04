import threading

sum = 0

loopSum=10000

lock = threading.Lock()

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁，申请锁
        lock.acquire()
        sum+=1
        #释放锁
        lock.release()
        print(sum)
def myM():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum-=1
        lock.release()
        print(sum)
def main():
    print("Start :{0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myM, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("end {}".format(sum))
if __name__ == '__main__':

    main()