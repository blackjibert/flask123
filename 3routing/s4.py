from flask import Flask, views, url_for
from werkzeug.routing import BaseConverter



app = Flask(__name__)


class RegexConverter(BaseConverter):
    """
        自定义URL匹配正则表达式
    """
    # 步骤1
    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    # 步骤2
    # 正则匹配成功之后，会执行to_python方法
    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        return int(value)  #把字符串强转为int，默认为字符串

    # 步骤3
    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        # return "888" # 这里也可以自定义操作
        return val
# 自定义一个转化器之后，flask是不知道有这个转化器，因此需要告诉flask
# 添加到flask中
app.url_map.converters['regex'] = RegexConverter


@app.route('/index/<regex("\d+"):nid>')
def index(nid):
    print(nid, type(nid))

    #反向生成
    # v=print(url_for('index', nid='888')) # /index/888
    # print(v)

    return 'Index'


if __name__ == '__main__':
    app.run()

