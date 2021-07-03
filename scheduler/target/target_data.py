# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    查询数据脚本，调用webapi接口
"""
__author__ = "HOU"

import pymysql
import requests
import json
from target_params import data_in, logger
from pandas import json_normalize


def post_data():
    """方法注释：
        获取计算所用数据,post 方式
    """
    url = "http://127.0.0.1:5000"
    headers = {'content-type': 'application/json'}
    requestData = {"certificate_no": "56565656565656", "auth_code": "123456"}
    ret = requests.post(url, json=requestData, data=headers)
    if ret.status_code == 200:
        data_json = json.loads(ret.text)['data']
        data_frame = json_to_dataframe(data_json)
        return data_frame
    else:
        logger.error(ret.status_code + ':' + ret.text)
        return None


def get_data():
    """方法注释：
        获取计算所用数据,get 方式
    """
    url = "http://127.0.0.1:5000"
    params = {'table_name', 'user'}
    ret = requests.get(url, params=params)
    if ret.status_code == 200:
        data_json = json.loads(ret.text)['data']
        data_frame = json_to_dataframe(data_json)
        return data_frame
    else:
        logger.error("没有数据" + ret.status_code + ':' + ret.text)
        return None


def json_to_dataframe(data_json):
    data_frame = json_normalize(data_json)
    return data_frame


def add_data():
    """方法注释：
        数据缓存，供下一步使用
    :return:
    """
    data_in['key'] = get_data()


def select_data1():
    # 打开数据库连接
    db = pymysql.connect(host='192.168.43.61', port=3306, user='root', password='314315', db='basedb',
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM sys_config")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    return data

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    get_data()
