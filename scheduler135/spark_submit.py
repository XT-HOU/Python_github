# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    04_spark 分布式计算功能
"""
__author__ = "HOU"


def get_cmd(executors='1', cores='2', memory='2G'):
    """方法注释:
        获取分布式计算命令
    :param executors: 设置启动的 executor 数量
    :param cores: driver使用的内核数
    :param memory: 每个 excutor 的内存
    :return:
    """
    cmd_submit = '04_spark-submit ' \
                 ' --master yarn' \
                 ' --deploy-mode cluster' \
                 ' --num-executors %s' \
                 ' --driver-cores %s' \
                 ' --executor-memory %s' % (executors, cores, memory)
    return cmd_submit


if __name__ == '__main__':
    pass
