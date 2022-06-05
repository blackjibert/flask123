from flask import Flask, Blueprint
"""
子域名
"""

app = Flask(__name__)
app.config["SERVER_NAME"] = 'oldboy. :5000'


@app.route("/dynamic", subdomain="<username>")
def index(username):
    print(username)
    return "index"

if __name__ == '__main__':
    app.run()

