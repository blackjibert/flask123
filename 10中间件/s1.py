from flask import Flask, session, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'sdfasdf'


@app.route('/x1', methods=['GET', 'POST'])
def x1():
    return '视图函数1'


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    return '视图函数2'

class Middleware(object):
    def __init__(self, old_wsgi_app):
        """
        服务端启动时，自动执行
        :param old_wsgi_app:
        """

        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        """
        每次有用户请求到来的时候，
        :param environ:
        :param start_response:
        :return:
        """

        print('before')    ##比如这里可以做一些黑名单
        obj = self.old_wsgi_app(environ, start_response)
        print('after')
        return obj


if __name__ == '__main__':
    app.wsgi_app = Middleware(app.wsgi_app)
    app.run()
    """
    1、执行app.__call__()方法
    2、再调用app.wsgi_app()方法
    """