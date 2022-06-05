from flask import Flask, request, render_template, Markup


app = Flask(__name__)


@app.template_global()
def sbbb(a1,a2):
    """
    每个模板中都可以调用的函数
    :param a1:
    :param a2:
    :return:
    """
    return a1 + a2

def get_input(value):
    # return "<input value='%s' />" % value
    return Markup("<input value='%s' />" % value)


@app.route('/show', methods=['GET', 'POST'])
def index():
    context = {
        'k1': 123,
        'k2': {11, 12, 23},
        'k3': {'name': 'oldboy', 'age': 312},
        'k4': lambda x: x+1,
        'k5': get_input
    }
    return render_template('index.html', **context)


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    context = {
        'k1': 123,
        'k2': {11, 500, 23},

    }
    return render_template('order.html', **context)





if __name__ == '__main__':
    app.run()