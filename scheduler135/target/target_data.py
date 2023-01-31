# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    查询数据脚本，调用webapi接口
"""
__author__ = "HOU"

import requests
import json
from target_params import data_in, logger, spark
from pandas import json_normalize


params = {'table_name': 'user'}


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

    ret = requests.get(url, params=params)
    if ret.status_code == 200:
        text = ret.text
        data_list = json.loads(text)['data']
        data_frame = json_to_dataframe(data_list)
        return data_frame
    else:
        logger.error("没有数据" + ret.status_code + ':' + ret.text)
        return None


def json_to_dataframe(data_list):
    # data_frame = json_normalize(data_list)

    sc = spark.sparkContext
    rdd = sc.parallelize(data_list)
    data_frame = spark.read.json(rdd)
    data_frame.show(10, 100)
    # data_frame.printSchema()
    return data_frame


def add_data():
    """方法注释：
        数据缓存，供下一步使用
    :return:
    """
    for item in params:
        data_in[item] = get_data()


if __name__ == "__main__":
    get_data()
