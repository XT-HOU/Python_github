# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    公共对象
"""
__author__ = "HOU"

import log
import spark
from lxml import objectify, etree


task = None
"""任务单信息 key"""
batch = set()
"""批次信息 key"""
vehicle = {}
"""架次信息 key-value"""
fighter_master = None
"""载机名称"""
fighter_target = None
"""目标机名称"""
beg_time = None
"""开始时间"""
end_time = None
"""结束时间"""
params = {}
"""配置参数 key-value"""
data_in = {}
"""输入数据 key-value"""
data_out = {}
"""输入数据 key-value"""
logger = log.get_logger()
"""日志对象"""
spark = spark.get_spark()
"""sparkSession"""


class Params(object):
    pass


def get_params():
    """方法注释：
        获取参数
    """
    cfg = etree.parse("config.xml")
    result = etree.tostring(cfg, pretty_print=True)
    xml = objectify.fromstring(result)

    for item in xml.param:
        param = Params()
        param.type = item.type
        param.name = item.name
        param.value = item.value
        if params.get(param.name) is None:
            params[param.name] = param.value


if __name__ == '__main__':
    get_params()
    print(params)
