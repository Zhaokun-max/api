#利用time延时函数，生成两个函数
#利用多线程调用
#计算总运行时间
#待参数的多线程启动方式
import time
# 导入多线程更名为_thread

import threading

def loop1(in1):
    # ctime得到当前时间
    try:
        print('Start loop l at:',time.ctime())
        # 把参数打印
        print("我是参数",in1)
        #睡眠时间，单位秒
        time.sleep(2)
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

def main():
    print("Start at",time.ctime())
    #生成threading.Theread实例
    t1 = threading.Thread(target=loop1, args=("padna",))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=loop2, args=("盼达","泽霖"))
    t2.start()
    t2.join()

    print("End at:",time.ctime())
if __name__ == "__main__":
    while True:
        main()
        break
    # 要有while语句
    # 因为启动多线程后本程序作为主线程序存在
    # 如果主程序执行完毕，则子线程可能也需要终止
