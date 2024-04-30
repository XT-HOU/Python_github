# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
    numpy 数组属性
"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# ndarray.ndim 用于返回数组的维数，等于秩。
print(a.ndim)
# ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。
# 比如，一个二维数组，其维度表示"行数"和"列数"。
print(a.shape)
# ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
print(a.itemsize)
# ndarray.flags 返回 ndarray 对象的内存信息
print(a.flags)
