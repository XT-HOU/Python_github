# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
"""
import numpy as np

# ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。
a = np.arange(10)
b = a[2:7:2]  # 从索引 2 开始到索引 7 停止，间隔为 2    start:stop(不包括停止索引):step
print(b)

# 多维数组索引
# 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素
# 整数数组索引是指使用一个数组来访问另一个数组的元素。这个数组中的每个元素都是目标数组中某个维度上的索引值。
x = np.array([[1, 2], [3, 4], [5, 6]])
# 获取数组中 (0,0)，(1,1) 和 (2,0) 位置处的元素
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

# numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
x = np.arange(9.).reshape(3, 3)
print('我们的数组是：')
print(x)
print('大于 3 的元素的索引：')
y = np.where(x > 3)
print(y)
print('使用这些索引来获取满足条件的元素：')
print(x[y])

# numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素。
x = np.arange(9.).reshape(3, 3)
print('我们的数组是：')
print(x)
# 定义条件, 选择偶数元素
condition = np.mod(x, 2) == 0
print('按元素的条件值：')
print(condition)
print('使用条件提取元素：')
print(np.extract(condition, x))
