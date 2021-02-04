#利用time延时函数，生成两个函数
#利用多线程调用
#计算总运行时间
#待参数的多线程启动方式
import time
# 导入多线程更名为_thread

import _thread as thread
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
    print('String at:',time.ctime())
#启动多线程的意思是多线程去执行某个函数
#启动多线程函数为start_new_thead
#参数两个,一个是需要运行的函数名,第二是函数的参数作为元组使用,为空则使用空元祖
#注意,如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ("panda",))

    thread.start_new_thread(loop2, ("盼达","泽霖"))
    print('All done at:',time.ctime())

if __name__ == "__main__":
    main()
    # 要有while语句
    # 因为启动多线程后本程序作为主线程序存在
    # 如果主程序执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(1)