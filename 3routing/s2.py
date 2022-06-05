from flask import Flask, url_for

"""
    反向生成URL，url_for
"""

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'], endpoint='n1')
def index():
    v1 = url_for('n1')     #用于反向生成，一个别名
    v1 = url_for('index')  #没有别名endpoint就是函数名
    print(v1)
    return 'index'


@app.route('/login', methods=['GET', 'POST'], endpoint='n2')
def login():
    return'login'


@app.route('/logout', methods=['GET', 'POST'], endpoint='n3')
def logout():
    return'logout'



if __name__ == '__main__':
    app.run()