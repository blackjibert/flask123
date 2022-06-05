参考：

    """
    博客参考：
    https://www.cnblogs.com/wupeiqi/articles/7552008.html
    
    """

Flask上下文管理
- 1、threading.local
- 2、上下文管理
- 3、数据库连接池


内容回顾
- 1、linux命令(20)
    cd, vim,  mkdir, ls, touch, cat, sed
- 2、（算法）堆排序
- 3、obj['x'] = 123 会触发__setitem__方法
- 4、obj['x'] = 123 会触发__setattr__方法
- 5、双下划线的的方法，__new__, __call__, __next__，__dict__
- 6、面向对象的特殊方法
- 7、functools
    偏函数functools.partial（）
    
    def func(a1, a2, a3):
        return a1 + a2 + a3
    v1 = func(1, 2, 3)
    
    new_func = functools.partial(func, 111)  #为函数自动传参
    new_func(2, 3)
    
    new_func = functools.partial(func, 111,2 )
    new_func(3)
    
- 8、装饰器？应用场景？
在不改变原来函数的代码之上，在函数的之前或者之后，定制一些功能。
- 应用：
 - flask：路由， before_request
 - django: csrf, 登录认证，django缓存
 
 
- 9、Flask
    蓝图：目录结构的管理，加url前缀，在某个蓝图里面加before_request
    session原理：flask和django中的session的区别，有一张图
 
### 二、内容详细
Flask上下文管理
- 1、threading.local
- 2、上下文管理
- 3、数据库连接池
### 详细   
- 多线程改一个全局变量，可能会出问题（锁机制）
- python中，




