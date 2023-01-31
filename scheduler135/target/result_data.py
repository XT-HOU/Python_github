# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    插入数据脚本，调用webapi接口
"""
__author__ = "HOU"

import json
import requests
from target_params import data_out, logger


def insert_data():
    """方法注释：
        插入计算数据
    """
    datadict = {}
    url = "http://127.0.0.1:5000/insert"
    for item in data_out:
        data_frame_json = data_out[item].to_json(orient="records")
        datadict[item] = data_frame_json
    data = json.dumps(datadict)
    ret = requests.post(url, data=data)
    if ret.status_code == 200:
        print(json.loads(ret.text)['msg'])
    else:
        logger.error(ret.status_code + ':' + ret.text)


if __name__ == '__main__':
    pass
