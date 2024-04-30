# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
"""
import random
import pandas as pd

data = pd.DataFrame()

for index in range(3):
    list = []
    for i in range(240):
        t = random.randint(0, 10)
        list.append(t)
    data[index] = list

data.to_csv('output.csv')