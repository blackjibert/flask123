
##情况1
# class Foo(object):#继承对象
#     pass
#
#
# obj = Foo()
# obj['xxx'] = 123  #会触发对象obj的__setitem__()方法


#下面就不会报错
class Foo1(object):
    def __setitem__(self, key, value):
        pass


obj1 = Foo1()
obj1['xxx'] = 123  #会触发对象obj的__setitem__()方法


## 情况2
class Foo3(dict): #继承dict
    pass


obj3 = Foo3()  #特殊的字典



