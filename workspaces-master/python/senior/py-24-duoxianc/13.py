import threading
import time
# python2中  form Queue import Queue
#python
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize()<1000:
                for i in range(100):
                    count+=1
                    msg="生成商品"+str(count)
                    #put是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Cousumer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize()>100:
                for i in range(3):
                    # get就是从queue取出一个值
                    msg = self.name + "消费" + queue.get()
                    print(msg)
            time.sleep(0.5)

if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(500):
        queue.put("初始化产品"+str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Cousumer()
        c.start()