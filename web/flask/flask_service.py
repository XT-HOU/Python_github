# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""

from flask import Flask, request
import server_source
import json
from gevent import pywsgi

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    data = server_source.select_data1()
    print(data)
    return json.dumps({'code': 200, 'data': data})


if __name__ == '__main__':
    # ip地址为空默认为本地地址，放到服务器时要为空
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    print('Service is start http on port 5000......')
    server.serve_forever()
    # app.run()
