

from flask import Flask, url_for

app = Flask(__name__)

"""
    传参数
"""

@app.route('/index/<int:nid>', methods=['GET', 'POST'])
def index(nid):
    print(nid, type(nid))
    url_for('index', nid=888)

    return "index"



if __name__ == '__main__':
    app.run()

# @app.route('/user/<username>')  # 字符串
# @app.route('/post/<int:post_id>')
# @app.route('/post/<float:post_id>')
# @app.route('/post/<path:path>')  #路径，一大串的路径url
# @app.route('/login', methods=['GET', 'POST'])


"""
常用路由系统有以上五种，所有的路由系统都是基于一下对应关系（转换器）来处理：


DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}

"""

