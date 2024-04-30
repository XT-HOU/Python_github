# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：因子分析算法

"""
import numpy as np
import pandas as pd

from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

import seaborn as sns
import matplotlib.pyplot as plt


# 导入数据
df = pd.read_csv(r'../../data/新航迹.csv', encoding='GBK')
df.head()

# 删除无关列
# df.drop(["Unnamed: 0"], axis=1, inplace=True)

# 查看是否有缺失值
df.isnull().sum()

# 删除缺失值
df.dropna(inplace=True)

# 因子分析可靠性检验
# KMO检验统计量是用于比较变量间简单相关系数矩阵和偏相关系数的指标
kmo_all, kmo_model = calculate_kmo(df)
# 巴特莱特球度检验
chi_square_value, p_value = calculate_bartlett_sphericity(df)

print("kmo_all:", kmo_all, end="\n\n")
print("kmo_model:", kmo_model, end="\n\n")
print("chi_square_value:", chi_square_value, end="\n\n")
print("p_value:", p_value)

# 探索性因子分析
fa = FactorAnalyzer(25, rotation=None)
fa.fit(df)

# 相关系数矩阵的特征根和特征向量
ev, v = fa.get_eigenvalues()
ev, v

# 根据特征根>1发现，可提取6个公因子

# 绘制碎石图，选择因子数
plt.scatter(range(1, df.shape[1] + 1), ev)
plt.plot(range(1, df.shape[1] + 1), ev)
plt.title('因子分析碎石图')
plt.xlabel('公因子')
plt.ylabel('特征根')
plt.grid()
plt.savefig('因子分析碎石图.jpg')
plt.show()

# 建立因子分析模型
fa_six = FactorAnalyzer(6, rotation="varimax")
fa_six.fit(df)

df_cm = pd.DataFrame(np.abs(fa_six.loadings_), index=df.columns)

plt.figure(figsize=(14, 14))
ax = sns.heatmap(df_cm, annot=True, cmap="BuPu")

# 设置y轴的字体的大小
ax.yaxis.set_tick_params(labelsize=15)

plt.title('因子分析热力图', fontsize='xx-large')
# 设置y轴标签
plt.ylabel('变量', fontsize='xx-large')
plt.savefig('因子分析热力图.jpg')
plt.show()
# 输出因子的载荷
print(fa_six.loadings_)

# 建立因子分析模型

fa_five = FactorAnalyzer(3, rotation="varimax")  # 根据6个公因子的热力图发现Factor6在每个变量上均无载荷。故调整为5个公因子。
fa_five.fit(df)

import seaborn as sns

df_cm = pd.DataFrame(np.abs(fa_five.loadings_), index=df.columns)

plt.figure(figsize=(14, 14))
ax = sns.heatmap(df_cm, annot=True, cmap="BuPu")

# 设置y轴的字体的大小
ax.yaxis.set_tick_params(labelsize=15)

plt.title('因子分析热力图', fontsize='xx-large')
# 设置y轴标签
plt.ylabel('变量', fontsize='xx-large')
plt.show()
# 方差累计贡献

fa_v = fa_five.get_factor_variance()
fa_dt = pd.DataFrame({
    "特征根": fa_v[0],
    "方差贡献率": fa_v[1],
    "方差累计贡献率": fa_v[2]
})

print(fa_dt)

# 计算因子得分
score = fa_five.transform(df)
print(score)

# 计算综合得分
x = score @ (fa_v[1])
result = pd.DataFrame({"综合得分":x, "行号":list(df.index)})
result.sort_values(by="综合得分", ascending=False, inplace=True)
print(result)