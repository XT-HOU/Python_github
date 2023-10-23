# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释： sklearn 识别手写体数字
"""

import matplotlib.pyplot as plt
from sklearn import datasets, svm

# 加载 digits 数据集
digits = datasets.load_digits()
aa = digits.images[0]
print(aa)
plt.imshow(aa, cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

plt.subplot(321)
plt.imshow(digits.images[1791], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(322)
plt.imshow(digits.images[1792], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(323)
plt.imshow(digits.images[1793], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(324)
plt.imshow(digits.images[1794], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(325)
plt.imshow(digits.images[1795], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(326)
plt.imshow(digits.images[1796], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
# svc估计器
svc = svm.SVC(gamma=0.001, C=100)
# svc 估计器进行学习
svc.fit(digits.data[1:1790], digits.target[1:1790])
# 预测
print(svc.predict(digits.data[1791:1796]))
# 实际值
print(digits.target[1791:1796])

pass
