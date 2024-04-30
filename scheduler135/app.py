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

from globals import app, app_list, logger
from xml_manage import app_xml_obj, app_judge, set_app_state
from default import Default
from cal_thread import app_thread
from app_ssh import get_source


@app.route('/appInfo', methods=['POST'])
def app_info():
    """方法注释：
    获取评估流程编排xml
    :return: 提交是否成功
    """
    bp_xml = request.form.get('xml')
    bp_model = app_xml_obj(bp_xml)
    if app_judge(bp_model):
        app_list.append(bp_model)
        return json.dumps({'result': Default.OK.value, 'msg': None})
    else:
        return json.dumps({'result': Default.NO.value, 'msg': Default.MSG_LEN.value})


@app.route('/appState', methods=['POST'])
def change_state():
    """方法注释：
        修改编排状态
    :return: 修改是否成功
    """
    app_state = request.form.get('app_state')
    app_id = request.form.get('app_id')
    msg = set_app_state(app_id, app_state)
    if msg is None:
        return json.dumps({'result': Default.OK.value, 'msg': msg})
    else:
        return json.dumps({'result': Default.NO.value, 'msg': msg})


@app.route('/serInfo', methods=['GET'])
def get_server_info():
    """方法注释：
    内存使用情况，磁盘使用情况，CPU 使用情况
    :return: json格式数据
    """
    data = get_source()
    return json.dumps(data)


@app.route('/getAppInfo', methods=['GET'])
def get_app_list():
    """方法注释：
        获取当前执行编排信息
    :return: json格式数据
    """
    data = []
    for app_item in app_list:
        data.append(str(app_item.__dict__))
    return json.dumps(data)


def main():
    """方法注释：
    启动 flask 服务
    """
    # 开始计算
    app_thread()
    # ip地址为空默认为本地地址，放到服务器时要为空
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    logger.info('Service is start http on port 5000......')
    server.serve_forever()


if __name__ == '__main__':
    main()
