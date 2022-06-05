#g是什么？比全局变量更牛
from flask import Flask, g, request

app = Flask(__name__)

@app.before_request
def bf():
    g.x = 66


@app.route('/n1')
def n1():
    print(g.x)
    return 'n1'


@app.route('n2')
def n2():
    print(g.x)
    return 'n2'


if __name__ == '__main__':
    app.run()