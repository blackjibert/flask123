from flask import Flask, request, session

app = Flask(__name__)


@app.route('/')
def index():
    print(request) #   request.__str__   LocalProxy.__str__
    # ctx中把request拿出来，再去request中获取method
    print(request.method)  # LocalProxy.__getattr__(key='method')
    # ctx中把request拿出来，再去request中获取args
    print(request.args)  # LocalProxy.__getattr__(key='args')

    #ctx中session,再去session中改k1设置值
    session['k1'] = 123   # LocalProxy.__setitem__(key='k1', value=123)

    # ctx中session，再去session中获取k1对应的值
    session['k1'] #LocalProxy.__getitem__(key='k1')
    return 'index'


if __name__ == '__main__':

    app.run()