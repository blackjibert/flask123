from flask import Flask, request
##请求相关的东西都在request里面

##返回的东西都有render_template, redirect


app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():

    #请求相关
    request.args
    return 'index'


    #响应相关

    return " "
    # return render_template('index.html', n1=123)
    # return redirect('/index')
    # return json.dumps({}) #return jsonify({})

    # response = make_response(render_template('index.html'))  #包装成respose，就可以进行如下的操作
    # response = make_response("xxx")
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response



if __name__ == '__main__':
    app.run()