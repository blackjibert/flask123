## session

字典序列化之后为字符串


#### 流程

用户访问服务器，服务器在内存中开辟一段空间，存放session，如果请求中有cookie则存放到session,
如果请求第一次来，则在session中创建cookie，然后接着访问视图函数，视图函数可以对session进行操作
视图函数处理完之后，给用户返回值，当即将断开连接的时候，会把session中的信息，字典序列化成字符串，
存到用户浏览器的cookie当中，同时，服务器的seesion信息进行销毁。

flask流程

- 1、服务器先运行起来，只要请求一到来，就会执行app的__call__方法
- 2、然后执行里面的wsgi_app(self, environ, start_response)
其中，environ就是原生的数据
ctx = RequestContext(app, environ)
request(environ),处理请求相关
session=None
ctx.push()是给session赋值，self.app.open_session(self.request)
层层看源码之后，session就是一个特殊的字典。



###session流程
1.请求刚刚到达，会创建一个ctx对象
ctx = RequestContext()
     request
     session= None
ctx.push() 会调用SecureCookieSessionInterfact.open_session
cts.session = SecureCookieSessionInterface.open_session

2.视图函数

3 请求结束
SecureCookieSessionInterface.save_session 再写道cookie里面