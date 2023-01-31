# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    dataframe操作
"""

import pandas as pd
from pyspark.sql import SparkSession

#
# def panda_dataframe():
#     # 查询
#     # df['column_name'] 和 df[row_start_index, row_end_index]
#     df['name']  # 选取单列
#     df['gender']
#     df[['name', 'gender']]  # 选取多列，多列名字要放在list里
#     df[0:]  # 第0行及之后的行，相当于df的全部数据，注意冒号是必须的
#     df[:2]  # 第2行之前的数据（不含第2行）
#     df[0:1]  # 第0行
#     df[1:3]  # 第1行到第2行（不含第3行）
#     df[-1:]  # 最后一行
#     df[-3:-1]  # 倒数第3行到倒数第1行（不包含最后1行即倒数第1行，这里有点烦躁，因为从前数时从第0行开始，从后数就是-1行开始，毕竟没有-0）
#     # df.loc[index, column_name],选取指定行和列的数据
#     df.loc[0, 'name']  # 'Snow'
#     df.loc[0:2, ['name', 'age']]  # 选取第0行到第2行，name列和age列的数据, 注意这里的行选取是包含下标的。
#     df.loc[[2, 3], ['name', 'age']]  # 选取指定的第2行和第3行，name和age列的数据
#     df.loc[df['gender'] == 'M', 'name']  # 选取gender列是M，name列的数据
#     df.loc[df['gender'] == 'M', ['name', 'age']]  # 选取gender列是M，name和age列的数据
#     # df.iloc[row_index, column_index]
#     df.iloc[0, 0]  # 第0行第0列的数据，'Snow'
#     df.iloc[1, 2]  # 第1行第2列的数据，32
#     df.iloc[[1, 3], 0:2]  # 第1行和第3行，从第0列到第2列（不包含第2列）的数据
#     df.iloc[1:3, [1, 2]]  # 第1行到第3行（不包含第3行），第1列和第2列的数据
#
#
# def pands_to_spark():
#     """
#         pandas dataframe 与 04_spark dataframe 互相转换
#     :return:
#     """
#     global values, columns
#     # pandas转spark
#     a = [['2', '1.2', '4.2'], ['0', '10', '0.3'], ['1', '5', '0']]
#     pandas_df = df(a, columns=['one', 'two', 'three'])
#     values = pandas_df.values.tolist()
#     columns = pandas_df.columns.tolist()
#
#     04_spark = SparkSession.builder.master("local[1]").appName("app_name").getOrCreate()
#     spark_df = 04_spark.createDataFrame(values, columns)
#     spark_df.show()
#     # spark转pandas
#     pandas_df = spark_df.toPandas()
#     print(pandas_df)


if __name__ == '__main__':
    a = [
        {'time': '19:56:10', '速度': '10', 'state': 'off'},
        {'time': '19:56:11', '速度': '20', 'state': 'off'},
        {'time': '19:56:12', '速度': '30', 'state': 'off'},
        {'time': '19:56:13', '速度': '30', 'state': 'off'},
        {'time': '19:56:14', '速度': '50', 'state': 'off'},
        {'time': '19:56:15', '速度': '60', 'state': 'off'},
        {'time': '19:56:16', '速度': '100', 'state': 'off'},
        {'time': '19:56:17', '速度': '120', 'state': 'off'},
        {'time': '19:56:18', '速度': '150', 'state': 'on'}
    ]

    df = pd.DataFrame(a)
    print(df)
    dfsa = df[(pd.to_numeric(df.速度) > 60) & (df.time > '19:56:16')].sort_values(by="time")
    # for row in df.itertuples():
    #     print(getattr(row, 'time'))
    print(df.to_dict(orient='records'))
