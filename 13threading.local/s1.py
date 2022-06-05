from threading import local, Thread
import time

#对比1
zhj = -1


def task(arg):
    global zhj
    zhj = arg
    time.sleep(2)
    print(zhj)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()






