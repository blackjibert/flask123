from flask import Flask, request, session

app = Flask(__name__)


@app.route('/')
def index():

    return 'index'


if __name__ == '__main__':

    app.__call__   #不加括号，不执行
    app.wsgi_app
    app.run()

"""
    1、请求一旦到来，执行app.__call__方法
    2、environ就是对请求来的时候，先行处理之后的结果
"""



