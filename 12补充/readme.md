#补充
## 1、项目依赖 pipreqs
- pip3 install pipreqs
- 生成依赖环境安装成功之后:执行pipreqs ./  [--force]
- 安装依赖环境 pip3 install -r requirements.txt
## 2、函数和方法的区别？
通过类去调用，是函数

通过对象去调用，是方法

    from types import MethodType, FunctionType
    
    class Foo(object):
        def fetch(self):
            pass
    
    
    print(Foo.fetch)  ##函数
    
    obj = Foo()
    print(obj.fetch) ##方法
    
    
    print(isinstance(obj.fetch, MethodType))
    print(isinstance(Foo.fetch, FunctionType)) #true
    
    
