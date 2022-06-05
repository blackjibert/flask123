## 对比2
import time
from threading import local, Thread
from threading import get_ident


##特殊的对象
zhj = local()
"""
作用：
    为每个线程开辟一段空间进行数据存储。
问题：
    自己通过字典创建要给类似于threading.local的东西
"""


def task(arg):
    #对象.value = 1/2/3/4/5/6/7/8
    zhj.value = arg
    time.sleep(2)
    print(zhj.value)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
