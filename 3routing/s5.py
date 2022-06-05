from flask import Flask
"""
其他参数

"""
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'], endpoint='n1', defaults={'db': "xxx"})   #defaluts和路由无关
def index(db):
    print(db)
    return "index"


##重定向
@app.route('/old', methods=['GET', 'POST'], redirect_to='/new') #老页面重定向新页面
def old():
    return "老功能"


@app.route('/new', methods=['GET', 'POST'])
def new():
    return "新功能"


##子域名




if __name__ == '__main__':
    app.run()