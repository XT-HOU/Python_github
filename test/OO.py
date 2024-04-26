# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"



class Test:
    def __init__(self):
        print('Test id is %d' % id(self))


if __name__ == '__main__':
    from pandas import DataFrame

    # 利用字典
    merge_dt_dict = {'开始时间戳': [1698661939,1698661960,1698661989,1698661955,1698661978,1698661964],
                     '结束时间戳': [1698661955,1698661980,1698661999,1698661970,1698661989,1698661999],
                     '分类列': ['分类1','分类1','分类1','分类2','分类2','分类3']}

    data_df = DataFrame(merge_dt_dict)


