# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

if __name__ == '__main__':
    from pandas import DataFrame

    df1 = DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],

                     'B': ['B0', 'B1', 'B2', 'B3'],

                     'C': ['C0', 'C1', 'C2', 'C3'],

                     'D': ['D0', 'D1', 'D2', 'D3']})

    df2 = DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],

                     'B': ['B4', 'B5', 'B6', 'B7'],

                     'C': ['C4', 'C5', 'C6', 'C7'],

                     'D': ['D4', 'D5', 'D6', 'D7']})
    df3 = DataFrame(columns=['A','B','C','D','E'])

    dfs = {'df1': {'df':df3},'df3':df1}

    df = dfs.get('df1')['df'].update(dfs.get('df3'))
    df = df2.update(df1)
    print(df)