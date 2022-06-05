## flask的装饰器
from flask import Flask, views
import functools
app = Flask(__name__)


def wapper(func):
    @functools.wraps(func)  #保留原信息
    def inner(*argsm, **kwargs):
        print("before")
        return func(*argsm, **kwargs)
    return inner


@app.route('/test', methods=['GET', 'POST'])
@wapper
def index():
    return 'index'
#上面三行代码是一个整体，他的函数名是inner

#FBV
@app.route('/test', methods=['GET', 'POST'])
@wapper
def order():
    return 'order'
# 上面三行代码的函数名也是inner，这样会报错，AssertionError: View function mapping is overwriting an existing endpoint function: inner
# 因此要引入functools，三行代码的函数命是自己的函数名字，也就是order

#
# #CBV 方式1
# class IndexView(views.View):
#     methods = ['GET']
#     decorators = [wapper,] #给所有的请求加装饰器
#
#     def dispatch_request(self): #反射
#         print('index!')
#         return 'index'
# app.add_url_rule('/index', view_func=IndexView.as_view(name='index')) #name=endpoint

#CBV 方式2 更方便
class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [wapper,]  #给所有的请求加装饰器

    def get(self):
        return 'index.GET'

    def post(self):
        return 'index.POST'

#添加路由
app.add_url_rule('/index', view_func=IndexView.as_view(name='index')) #name=endpoint





if __name__ == '__main__':
    app.run()