import multiprocessing
from time import ctime
#消费者
def consumer(input_q):
    print("into consumer:", ctime())
    while True:
        #处理项
        itme = input_q.get()
        print("pull", itme, "out of q")# 此处替换为有用的工作
        input_q.task_done()# 发出信号通知任务完成
    print("out of consumer:", ctime())# 此句未执行，因为q.join收到四个task_done（）信号后，主进程启动，未等到print此句完成
    #生产者
def producer(seqence, output_q):
    print("into procuder:", ctime())
    for item in seqence:
        output_q.put(item)
        print("put", item, "into q")
    print("out of procuder:", ctime())


# 建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    # 守护进程
    cons_p.daemo = True
    cons_p.start()
    # 生产多个项，sequence代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或通过一些其它方式生产出来
    seqence = [1,2,3,4]
    producer(seqence, q)
    #等待所有项被处理
    q.join()