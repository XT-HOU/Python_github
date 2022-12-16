# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

import pandas as pd


def save_hive(file_name):
    # 要读取的文件列表
    # 写入的表名
    print('123')
    df_data = pd.read_excel(file_name)
    print(df_data)
    pass


if __name__ == '__main__':
    save_hive('../../data/myData.xlsx')