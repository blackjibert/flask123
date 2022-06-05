# 3 路由

## 路由内容详细
- s1 添加路由的两种方式
- s2 endpoint(没有的话，就是默认函数名)
- s3 传参数
- s4 自定义正则参数
- s5 其他参数


## s1 添加路由的两种方式
程序先启动起来，把url和视图函数对应起来，等着请求来，把请求头里的url拿过来，去路由表
里面去匹配。
 @app.route('/index', methods=['GET', 'POST'])
def index():
    return 'index'
    
从上到下执行，返回一个值，app.route返回一个函数decorator    
点进去@app.route里面发现是这样的

    def route(self, rule: str, **options: t.Any) -> t.Callable:
        #rule ='/index',options={methods=['GET', 'POST']}
        def decorator(f: t.Callable) -> t.Callable:
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

## s2 endpoint 
- enpoint 相当于django的name，有name就可以反向生成(别名)，不起别名，就是函数名字。
django的反向生成是reverse，flask的反向生成是url_for。


## s3传参数
-uuid 根据主板，时间，计算一个唯一标识，重复的几率很小。


## s4自定义正则参数

## s5其他参数

### 重定向
- 老页面重定向到新页面
- 前端中的重定向
    - meta
    - js

### s6子域名
比如detailer.autohome.com.cn和mail.autohome.com.cn
本地有一个hosts文件， 里面有ip和域名的对应。会先在本地的hosts通过域名查找ip


##总结
路由关系就是Rule对象，把rule放到url_map里面了，

self.url_map() = Map
map=[
    Rule(''=/index', 函数)，
    Rule(''=/index', 函数)，
    Rule(''=/index', 函数)，
]

重点在于：
- url
- methods
- endpoint 默认函数名字
- @app.route('/index/<int:nid>/<int:nid2>/')
- url_for  反向生成
- 其他参数




