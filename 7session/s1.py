from flask import Flask, session

app = Flask(__name__)
app.secret_key = '123lkhdfs'


@app.route('/x1', methods=['GET', 'POST'])
def x1():
    #去ctx中获取session
    session['k1'] = 123  #会触发__setitem__方法，获取的话会触发__getitem__方法，字典也可以用这种方法
    return 'index'


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    print(session['k1'])
    return 'Order'


if __name__ == '__main__':
    app.run()