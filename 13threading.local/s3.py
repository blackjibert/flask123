## 对比2
import time
from threading import local, Thread
from threading import get_ident


##特殊的对象
zhj = local()

def task(arg):
    #线程的唯一标记
   print(get_ident())  #


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
