# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
    NumPy 创建数组
"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

# numpy  创建数组
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
x = np.empty([3, 2], dtype=int)
print(x)
# numpy.zeros 创建指定大小的数组，数组元素以 0 来填充
x = np.zeros(5)
print(x)
# numpy.ones 创建指定形状的数组，数组元素以 1 来填充
x = np.ones((3, 2), dtype=int)
print(x)
# numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充
zeros_arr = np.zeros_like(a)
print(zeros_arr)
# numpy.ones_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充。
ones_arr = np.ones_like(a)
print(ones_arr)

# NumPy 从已有的数组创建数组
x = [1, 2, 3]  # 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
a = np.asarray(x)
print(a)
# numpy.frombuffer 用于实现动态数组。接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象
s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)
print((a[0]).decode('utf-8'))
# numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
list = range(5)
# 使用迭代器创建 ndarray
x = np.fromiter(list, dtype=float)
print(x)

# NumPy 从数值范围创建数组
# numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象 numpy.arange(start, stop, step, dtype)
# start	起始值，默认为0 stop	终止值（不包含） step	步长，默认为1
x = np.arange(5)
print(x)
x = np.arange(10, 20, 2)
print(x)
# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
a = np.linspace(10, 20, 5, endpoint=False)
print(a)
# numpy.logspace 函数用于创建一个于等比数列。/
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)  base对数 log 的底数。
# 默认底数是 10
a = np.logspace(1.0, 2.0, num=10)
print(a)
