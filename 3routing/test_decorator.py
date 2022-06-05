## flask的装饰器
from flask import Flask
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


@app.route('/test', methods=['GET', 'POST'])
@wapper
def order():
    return 'order'
# 上面三行代码的函数名也是inner，这样会报错，AssertionError: View function mapping is overwriting an existing endpoint function: inner
# 因此要引入functools，三行代码的函数命是自己的函数名字，也就是order


if __name__ == '__main__':
    app.run()
