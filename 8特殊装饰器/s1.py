from flask import Flask, session

app = Flask(__name__)


"""
before_request =  [before1,before2]
"""

@app.before_request
def before1():
    print('执行前1')


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


@app.route('/x1', methods=['GET', 'POST'])
def x1():
    print('视图函数1')
    return '视图函数1'


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    print('视图函数2')
    return '视图函数2'


if __name__ == '__main__':
    app.run()