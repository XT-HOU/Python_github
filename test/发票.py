# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

# encoding: utf-8
import time
import random
import matlab

a1=(2021,10,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(2021,11,30,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳

#随机生成10个日期字符串
for i in range(240):
    t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple=time.localtime(t)          #将时间戳生成时间元组
    date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    print(date)

print('---------------------')
import datetime,random
def randomtimes(start, end, n, frmt="%H:%M"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    time_datetime=[random.random() * (etime - stime) + stime for _ in range(n)]
    for t in time_datetime:
        print(t.strftime(frmt))
    # time_str=[t.strftime(frmt) for t in time_datetime]
    # print(time_str)
randomtimes('07:00','21:00',240)
print('---------------------')
import numpy as np

for i in range(240):

    number = np.random.uniform(280.0, 320.0)
    print(round(number,0))

