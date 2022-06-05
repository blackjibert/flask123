
##重要
import time
from threading import get_ident, Thread
try:
    from greenlet import getcurrent as get_ident  #协程

except Exception as e:
    from threading import Thread,get_ident
##自定义Local对象(基于协程，也就是微线程)


class Local(object):

    def __init__(self):

        # self.storage = {}
        object.__setattr__(self, 'storage', {}) #父类里面有__setattr__

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return self.storage[ident][k]


"""
{
    1233:{val:1}
}
"""
obj = Local()

"""
{
    1233:{xx:1}
}
"""

obj1 = Local()

##实现了一个类似Threading.local的功能
def task(arg):
    obj.val = arg      #obj.val 会触发__setattr__方法
    time.sleep(2)
    # v = obj["val"]
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()