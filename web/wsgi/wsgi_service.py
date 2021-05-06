# ！/usr/bin/python3
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from wsgi_client import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('192.168.43.234', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
