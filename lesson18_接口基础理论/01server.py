'''
模拟后端接口
'''
from flask import Flask

server = Flask(__name__)


@server.route('/')
def index():
    return {'msg': "success", "data": "welcome to kt03"}


@server.route('/login/0728')
def login():
    return """<p style="color:red">反思自己不如指责他人</p>"""


if __name__ == '__main__':
    server.run(debug=None)
