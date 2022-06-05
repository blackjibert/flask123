from flask import Flask, session, request, session, redirect
app = Flask(__name__)
"""
常见的其他装饰器,@app.before_first_request, @app.errorhandler(404)
"""


@app.before_first_request
def before_first1():
    print("before_first_request1")


@app.before_first_request
def before_first2():
    print("before_first_request2")

@app.before_request
def before2():
    print('执行前2')


"""
after_request =  [after1,after2]
[after1,after2]会反转一下，reversed(after_request)

"""


@app.after_request
def after1(response):
    print('执行后1')
    return response


@app.after_request
def after2(response):
    print('执行后2')
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('视图函数1')
    return '视图函数1'


@app.route('/index', methods=['GET', 'POST'])
def x2():
    print('视图函数2')
    return '视图函数2'


@app.errorhandler(404)
def page_not_found(error):
    return 'page does not exist', 404


if __name__ == '__main__':
    app.run()