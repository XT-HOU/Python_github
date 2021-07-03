# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    算法脚本
"""
__author__ = "HOU"
import pandas as pd
from target_params import data_in, data_out, logger


def creat_data_frame():
    """方法注释：
        创建表结构
    """
    # data_frame = df({'name': 'hou', 'sex': 'nan', 'age': '18'}, columns=['name', 'sex', 'age'], index=[0])
    data_frame = pd.DataFrame(columns=['姓名', 'sex', 'age'])
    return data_frame


def target_caluate():
    """方法注释：
        指标计算步骤
    """
    df = creat_data_frame()
    # 计算用到的数据
    data = data_in['key']
    if data == None:
        logger.error("没有数据")
        return
    # data_frame.loc[0] = ['xx', 'xx', 'xx']
    df_insert = pd.DataFrame({'姓名': ['mason', 'mario'], 'sex': ['m', 'f'], 'age': [21, 22]})
    data_frame1 = df.append(df_insert, ignore_index=True)
    # df_insertone = {'姓名': 'hou', 'sex': 'nan', 'age': 20}
    # data_frame2 = data_frame1.append(df_insertone, ignore_index=True)
    data_out['table_name'] = data_frame1


if __name__ == '__main__':
    dataq = data_out['table_name'].query('age > 20')
    print(dataq)
