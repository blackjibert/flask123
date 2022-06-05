import time
from threading import get_ident, Thread

##自定义Local对象(基于面向对象3)


class Local(object):

    def __init__(self):

        # self.storage = {}
        object.__setattr__(self, 'storage', {}) #父类里面有__setattr__

    def __setattr__(self, k, v):
        ident = get_ident()   #唯一标记通过线程得出
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