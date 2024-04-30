# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：曲线拟合
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# 定义要拟合的函数形式（这里选取二次多项式）
def func(x, a, b, c):
    return a * x ** 2 + b * x + c


# 生成随机样本点作为输入数据
np.random.seed(0)
x = np.linspace(-10, 10, 50)
y = func(x, 3, -4, 7) + np.random.normal(size=len(x))

# 调用 curve_fit() 函数进行曲线拟合
params, _ = curve_fit(func, x, y)
a, b, c = params
print("拟合参数：", params)

# 可视化结果
plt.scatter(x, y, label='Data')
plt.plot(x, func(x, a, b, c), 'r', label='Fit Curve')
plt.legend()
plt.show()