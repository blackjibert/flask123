import time
from threading import get_ident, Thread

##自定义Local对象(基于面向对象2)


class Local(object):
    storage = {}

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return Local.storage[ident][k]


obj = Local()

def task(arg):
    obj.val = arg      #obj.val 会触发__setattr__方法
    time.sleep(2)
    # v = obj["val"]
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()