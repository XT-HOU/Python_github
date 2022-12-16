# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

import pandas as pd
import random
import numpy as np
from scipy import interpolate


def create_DF():
    index = [1, 3, 5, 7, 9,
             11, 13, 15, 17, 19,
             21, 23, 25, 27, 29,
             31, 33, 35, 37, 39, ]
    names = [''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5)) for i in range(len(index))]
    ages = [11, 13, 15, 17, 19,
             21, 23, 25, 27, 29,
             31, 33, 35, 37, 39,
            41, 43, 45, 47, 49]
    citys = [''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)) for i in range(len(index))]
    genders = [random.choice(['m', 'wm']) for i in range(len(index))]

    df = pd.DataFrame({'index': index, 'name': names, 'age': ages, 'city': citys, 'gender': genders})
    # print(type(df['date']))
    # print(df)
    return df


def custom_interpolate():
    pass


if __name__ == '__main__':
    df = create_DF()
    print(df)
    print(df.sample(n=50,replace=False,axis=0))
    x = df['index']
    y = df['age']
    print(y)
    tckfun = interpolate.splrep(x, y, k=3)
    print(type(tckfun))
    print(tckfun)
    xx = np.linspace(1, 50, 10)
    print(type(xx))
    print(xx)
    value = interpolate.splev(xx, tckfun, der=0)
    print(value)
