from flask import Flask, session, flash, get_flashed_messages
"""
闪现： 
方式1：session
方式2：flash
"""


app = Flask(__name__)
app.secret_key = 'sdfasdf '

@app.route('/x1', methods=['GET', 'POST'])
def x1():

    # session['msg'] = '你好哇'
    flash('我是发', category='x1')
    flash('我是士大夫发', category='x2')
    return '视图函数1'


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    # msg = session.pop('msg')
    # print(msg)
    data = get_flashed_messages(category_filter=['x1'])  #拿出，就没有了
    print(data)
    return '视图函数2'


if __name__ == '__main__':
    app.run()