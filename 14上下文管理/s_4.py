#私有字段

class Foo(object):
    def __init__(self):
        self.__age = 18



obj = Foo()
v = obj._Foo__age  #调用私有字段_类名

print(v)