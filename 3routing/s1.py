from flask import Flask
"""
添加路由的两种方式
"""

app = Flask(__name__)


"""
1. 执行decorator = app.route('/index', methods=['GET', 'POST'])
2. @decorator
      - 新index =  decorator(index)

"""
#路由方式1（装饰器）:
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'index'


"""
#路由方式2（本质）：
本质是app.add_url_rule('/order', view_func=order) #等价于方式1
"""
def order():
    return "order"

app.add_url_rule('/order', view_func=order) #等价于方式1


if __name__ == '__main__':
    app.run()