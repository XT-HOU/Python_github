# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    定义函数执行顺序
    TODO：考虑自定义算子如何执行，按设计图顺序动态生成脚本
"""
__author__ = "HOU"

from target_data import get_data
from result_data import insert_data
from algorithm import target_caluate

if __name__ == '__main__':
    get_data()
    target_caluate()
    insert_data()
