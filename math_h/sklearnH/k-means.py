# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    K-means算法是很典型的基于距离的聚类算法，采用距离作为相似性的评价指标，即认为两个对象的距离越近，其相似度就越大。
其基本思想是：以空间中k个点为中心进行聚类，对最靠近他们的对象归类。通过迭代的方法，逐次更新各聚类中心的值，直至得到最好的聚类结果。
各聚类本身尽可能的紧凑，而各聚类之间尽可能的分开。
    算法大致流程为：
    1.随机选取k个点作为种子点(这k个点不一定属于数据集)；
    2.分别计算每个数据点到k个种子点的距离，离哪个种子点最近，就属于哪类；
    3.重新计算k个种子点的坐标(简单常用的方法是求坐标值的平均值作为新的坐标值；
    4.重复2、3步，直到种子点坐标不变或者循环次数完成。

各输入参数的含义
    n_clusters : int, optional, default: 8
表示的是要生成的簇的数量，或者说聚类中心的数量。是个整型的数，默认值为8；
    init : {‘k-means++’, ‘random’ or an ndarray}
表示的是对需要聚类的数据的初始化的方法，默认的方法是’k-means++’.
初始化的方法有三种：k-means++，random，或者是一个数组。
k-means++能智能的选择初始聚类中心进行k均值聚类，加快收敛速度。
random则是从数据中随机的选择k个观测值作为初始的聚类中心。
也可以传递给init一个数组作为初始化的聚类中心，则这个数组的结构应该是（n_clusters, n_features）。
    n_init : int, default: 10
表示的是K-means算法选择聚类中心的次数，默认值为10。最终返回的是聚类中心最好的一次结果（好是指时间的长短）。
    max_iter : int, default: 300
每次运行K-means算法的最大迭代次数，默认值为300.
    tol : float, default: 1e-4
表示的相当于是迭代终止的精度要求，可以允许的误差，当满足这个精度，则聚类收敛，寻找到最优解，可以停止迭代，默认值为10-4。
    precompute_distances : {‘auto’, True, False}
预先计算距离，在空间和时间上作出权衡。这样做会更快，但是会占用更多的内存，默认值为‘auto’。
‘auto’指如果n_samples * n_clusters > 12亿时，就不预先计算距离。这样就相当于使用双精度的每个作业大约需要100MB的内存。
‘True’指总是预先计算距离。
‘False’指不预先计算距离。
    verbose : int, default 0
是否输出详细信息，默认值为0。
    random_state : int, RandomState instance or None (default)
确定聚类中心初始化的随机数生成。使用一个整型的数是的随机性具有确定性，默认值为None。
    copy_x : boolean, optional
bool 在scikit-learn 很多接口中都会有这个参数的，就是是否对输入数据继续copy 操作，以便不修改用户的输入数据，默认值为True。
为True时，是不修改原始数据，确保X是C-contiguous，聚类后不修改原始数据。为False时，则修改原始数据，在函数返回之前将修改后的放回X，
但通过减去再加上数据均值，可能会引入较小的数值差异，在这种情况下，也不能保证数据是C-contiguous，可能会使速度明显的下降。
    n_jobs : int or None, optional (default=None)
使用进程的数量，与电脑CPU有关。默认值为None。
    algorithm : “auto”, “full” or “elkan”, default=“auto”
K-means算法所用到的，“full”指经典的EM-style算法；“elkan”通过使用三角不等式，所以更高效，但目前不支持稀疏的数据；“auto”则在数据密集时，
选择“elkan”，在数据稀疏时，选择“full”。

函数返回值
**cluster_centers_：**聚类中心的坐标。
如果算法还未完全收敛就停止，则将与labels_不一致。
**labels_：**每个点的标签。
**inertia_：**样本到聚类中心的平方和。
**n_iter_：**迭代运行的次数。

"""
__author__ = "HOU"

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import time


def demo01():
    data = np.array([[4, 2], [1, 2], [1, 4], [1, 0], [1, 3], [4, 4], [4, 0], [5, 2]])
    kmeans = KMeans(n_clusters=2, random_state=0).fit(data)
    df_insert = pd.DataFrame({'中心坐标': [str(kmeans.cluster_centers_)], '每个点的标签': [str(kmeans.labels_)]})

    return df_insert.to_json(orient='records',force_ascii=False)


def demo02():
    from sklearn.metrics.pairwise import pairwise_distances_argmin
    from sklearn.datasets._samples_generator import make_blobs
    import matplotlib.pyplot as plt

    # np.random.seed(0)
    centers = [[1, 1], [-1, -1], [1, -1]]
    n_clusters = len(centers)
    X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.7)
    # plot result
    fig = plt.figure(figsize=(8, 3))
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
    colors = ['#4EACC5', '#FF9C34', '#4E9A06']

    # original data
    ax = fig.add_subplot(1, 2, 1)
    row, _ = np.shape(X)
    for i in range(row):
        ax.plot(X[i, 0], X[i, 1], '#4EACC5', marker='.')

    ax.set_title('Original Data')
    ax.set_xticks(())
    ax.set_yticks(())

    # plt.show()
    # compute clustering with K-Means
    k_means = KMeans(init='k-means++', n_clusters=3, n_init=10)
    t0 = time.time()
    k_means.fit(X)
    t_batch = time.time() - t0

    k_means_cluster_centers = np.sort(k_means.cluster_centers_, axis=0)
    k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)

    # K-means
    ax = fig.add_subplot(1, 2, 2)
    for k, col in zip(range(n_clusters), colors):
        my_members = k_means_labels == k  # my_members是布尔型的数组（用于筛选同类的点，用不同颜色表示）
        cluster_center = k_means_cluster_centers[k]
        ax.plot(X[my_members, 0], X[my_members, 1], 'w',
                markerfacecolor=col, marker='.')  # 将同一类的点表示出来
        ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                markeredgecolor='k', marker='o')  # 将聚类中心单独表示出来
    ax.set_title('KMeans')
    ax.set_xticks(())
    ax.set_yticks(())
    plt.text(-3.5, 1.8, 'train time: %.2fs\ninertia: %f' % (t_batch, k_means.inertia_))

    plt.show()
    pass


if __name__ == '__main__':
    # print(demo01())
    demo02()
    pass
