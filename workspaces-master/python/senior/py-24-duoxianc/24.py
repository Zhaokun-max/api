import multiprocessing
from time import ctime
#消费者
def consumer(input_q):
    print("into consumer:", ctime())
    while True:
        #处理项
        itme = input_q.get()
        if itme is None:
            break
        print("pull", itme, "out of q")
    print("out of consumer:",ctime())# 此句执行完成，在转入主进程


    #生产者
def producer(seqence, output_q):
    print("into procuder:", ctime())
    for item in seqence:
        output_q.put(item)
        print("put", item, "into q")
    print("out of procuder:", ctime())


# 建立进程
if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.start()
    cons_p2.start()

    # 生产多个项，sequence代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或通过一些其它方式生产出来
    seqence = [1,2,3,4]
    producer(seqence, q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()