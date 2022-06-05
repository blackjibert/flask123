##上下文管理本质分析(s1.py)
网站本质是socket，请求来的时候是一个字符串（继续学习，不太懂）发的数据.-r,-n


请求来的时候，数据是-r,-n，服务器可以把请求数据分割一下,比如这种，request.meta,,,
那么谁来做这件事，wsgi来做这种事情，wsgi不属于web框架，是外聘来的。wsgi拿到原生的字符串之后，进行分割，
分割完之后，wsgi有一个environ参数，这里就是请求的数据，这里分的还不够细。接下来会有下一部分的
处理，得到这种request.meta很细的参数。打包起来，让服务器用起来比较方便。

ctx = self.request_context(environ)    
然后返回了一个对象，return RequestContext(self, environ)
RequestContext这个对象有request,有session,还有一个路由匹配
RequestContext中还有路由匹配（def match_request(self) ），根据url找到视图函数
ctx.push() ##打包,给session赋值(去cookie中获取值，并赋值)

{   
     x1:{"stack":[ctx(request, session),]},
     x2:{"stack":[ctx(request, session),]},
}

上下文管理就是把东西放在那里，用的时候再取。

首先，我们明确桥梁的作用，WSGI存在的目的有两个： 让Web服务器知道如何调用Python应用程序，
并且把用户的请求告诉应用程序。 让Python应用程序知道用户的具体请求是什么，
以及如何返回结果给Web服务器。
 
## 1、第一阶段请求到来处理阶段，将ctx(request, session)放到Local对象(根据线程不同，开辟空间)
第一个阶段，请求来的时候，去执行__call__方法，然后是wsgi_app()函数
wsgi_app()主要：
- ctx = self.request_context(environ)
- ctx.push()  push执行的是_request_ctx_stack.push()
打包到ctx中，包含有session和request  
看图1：local里面用的stack，为什么用stack?

### 问题：Flask中session什么时候创建，什么时候销毁？
当请求刚进来的时候，会将request和session，封装成一个RequestConetext()对象，接下来，把这个对象通过localstack放入内部一个local对象中，
最开始ctx中的session是空的，open_session将cookie中的值，复制到ctx中去， 中间进行操作，最后，将ctx中的session读出来，序列化，给用户写到cookie中，然后把
ctx移除掉。

## 2、第二阶段：视图函数导入阶段:request/session



## 3、第三阶段：请求处理完毕
- 获取session并保存到cookie
- 将ctx删除


## 机制支持多线程
并不会创建多个_app_ctx_stack = LocalStack()
只是在Local()中多了几条数据而已。


## 问题：Flask中总共有几个LocalStack和Local对象？
两个LocalStack，两个Local
request、session共同用一个LocalStack和Local
g、app共同用一个Localstack和Local


参考链接：https://www.cnblogs.com/ls13691357174/p/10001095.html

##作业

- 画Flask上下文管理 请求流程图(Process on)







