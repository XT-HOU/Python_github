# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"
import pandas as pd
import random
from datetime import datetime, timedelta

s_date = datetime(2020, 4, 1)
e_date = datetime(2020, 4, 1)


def create_DF():

    dates = ['00:00:01.104','00:00:01.105','00:00:01.106','00:00:01.107','00:00:01.108',
             # '00:00:01.109','00:00:01.110','00:00:01.111','00:00:01.112','00:00:01.113',
             # '00:00:02.104','00:00:02.105','00:00:02.106','00:00:02.107','00:00:02.108',
             '00:00:02.109','00:00:02.110','00:00:02.111','00:00:02.112','00:00:02.113']
    names = [''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5)) for i in range(len(dates))]
    ages = [random.randint(10, 71) for i in range(len(dates))]
    citys = [''.join(random.sample('13649678469', 2)) for i in range(len(dates))]
    genders = [random.choice(['m', 'wm']) for i in range(len(dates))]

    df = pd.DataFrame({'日期': dates, 'name': names, 'age': ages, 'city': citys, 'gender': genders})
    # print(type(df['date']))
    # print(df)
    return df
def create_DF1():

    dates = ['00:00:01.104','00:00:01.105','00:00:01.106','00:00:01.107','00:00:01.108',
             # '00:00:01.109','00:00:01.110','00:00:01.111','00:00:01.112','00:00:01.113',
             # '00:00:02.104','00:00:02.105','00:00:02.106','00:00:02.107','00:00:02.108',
             '00:00:02.109','00:00:02.110','00:00:02.111','00:00:02.112','00:00:02.113']
    names = [''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5)) for i in range(len(dates))]
    ages = [random.randint(10, 71) for i in range(len(dates))]
    citys = [''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)) for i in range(len(dates))]
    genders = [random.choice(['m', 'wm']) for i in range(len(dates))]

    df = pd.DataFrame({'date1': dates, 'name1': names})
    # print(type(df['date']))
    # print(df)
    return df

if __name__ == '__main__':



    df = create_DF()
    a = df.iloc[0]
    a.日期
    df[df.age >= 10]
    df1 = pd.DataFrame({'date1': df , 'name1': 'names'})
    aa = '00:00:02:110'
    print(type(-123.564))
    df = create_DF()
    df['age'] = df['age']/100
    print(df)
    # 生成一个分组桶，我这里是每3天作为一个组，按照date对数据进行标记
    # res = df.sample(n=5,replace=False,axis=0)


