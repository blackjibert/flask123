##函数和方法的区别
from types import MethodType, FunctionType


class Foo(object):
    def fetch(self):
        pass


print(Foo.fetch)  ##函数

obj = Foo()
print(obj.fetch) ##方法


print(isinstance(obj.fetch, MethodType))
print(isinstance(Foo.fetch, FunctionType)) #true