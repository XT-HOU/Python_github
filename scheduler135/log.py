# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    记录日志
"""
__author__ = "HOU"

import logging
import os.path
import time


def get_logger():
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # 日志文件输出
    logger.addHandler(get_fh_file())
    # 日志控制台输出
    logger.addHandler(get_fh_console())
    return logger


def get_fh_console():
    # 创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
    # 第四步和第五步分别加入以下代码即可
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    return ch


def get_fh_file():
    """方法注释：输出到文件
        定义日志输出路径及日志格式
    """
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/logs/'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + rq + '.log'
    logfile = log_name
    open(logfile, 'a')
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    return fh


if __name__ == '__main__':
    # 日志
    logger = get_logger()
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')