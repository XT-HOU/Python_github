# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    flask
"""
__author__ = "HOU"

import service
import json

from gevent import pywsgi
from flask import request

from globals import app, app_list
from xml_manage import app_xml, app_judge
from default import Default
from cal_thread import app_thread


@app.route('/serInfo', methods=['GET'])
def get_server_info():
    """方法注释：
    内存使用情况，磁盘使用情况，CPU 使用情况
    :return: json格式数据
    """
    data = service.get_server_info()
    return json.dumps(data)


@app.route('/appInfo', methods=['POST'])
def app_info():
    """方法注释：
    获取评估流程编排xml
    :return: 提交是否成功
    """
    bp_xml = request.form.get('xml')
    bp_model = app_xml(bp_xml)
    if app_judge(bp_model):
        app_list.append(bp_model)
        return json.dumps({'result': Default.OK.value, 'msg': None})
    else:
        return json.dumps({'result': Default.OK.value, 'msg': Default.MSG_LEN.value})


def main():
    """方法注释：
    启动 flask 服务
    """
    # 开始计算
    app_thread()
    # ip地址为空默认为本地地址，放到服务器时要为空
    server = pywsgi.WSGIServer(('', 5000), app)
    print('Service is start http on port 5000......')
    server.serve_forever()


if __name__ == '__main__':
    main()
