from flask import Flask, redirect, render_template

app = Flask(__name__)

#开发环境，测试环境，配置文件都是不一样的
# app.config.from_object("python类或类的路径") #配置文件的路径
app.config.from_object("settings.DevelopmentConfig") #配置文件的路径


@app.route('/index', methods=['GET', 'POST'])
def index():

    return 'asdf'
    # return redirect
    # return render_template()


if __name__ == '__main__':
    app.run()