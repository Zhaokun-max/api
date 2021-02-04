import threading
import time

def fun():
    print("I AM RUNNING.......")
    time.sleep(4)
    print("i an done")

if __name__ == '__main__':
    t = threading.Timer(6, fun)
    t.start()

    i = 0
    while True:
        print("{0}..........".format(i))
        time.sleep(2)
        i += 1