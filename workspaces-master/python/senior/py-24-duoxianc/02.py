'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread
def loop1():
    # ctime得到当前时间
    try:
        print('Start loop l at:',time.ctime())
        #睡眠时间，单位秒
        time.sleep(2)
        print('End loop l at:',time.ctime())
    except:
        print("eeeeee")
def loop2():
    try:
        # ctime得到当前时间
        print('Start loop 2 at:',time.ctime())
        #睡眠时间，单位秒
        time.sleep(2)
        print('End loop 2 at:',time.ctime())
    except:
        print("xxxxxx")
def main():
    print('String at:',time.ctime())

    #启动多线程的意思是多线程去执行某个函数
    #启动多线程函数为start_new_thead
    #参数两个,一个是需要运行的函数名,第二是函数的参数作为元组使用,为空则使用空元祖
    #注意,如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ())

    thread.start_new_thread(loop2, ())
    print('All done at:',time.ctime())


if __name__ == "__main__":
    main()
    while True:
        time.sleep(1)