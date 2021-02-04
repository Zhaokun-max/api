from multiprocessing import Process
import os


def info(title):
    print(title)
    print("modle name:",__name__)
    # 得到父亲进程id
    print("parent process", os.getpid())
    # 得到本身进程id
    print("process id:",os.getppid())

def f(name):
    info("function f")
    print("hello ", name)

if __name__ == '__main__':
    info("mian line")
    p = Process(target=f, args=("job",))
    p.start()
    p.join()