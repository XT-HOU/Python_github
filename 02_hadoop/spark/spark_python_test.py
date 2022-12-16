# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    spark执行的python脚本
"""
import time
import datetime
import math
import os
# from pyspark import SparkContext


def spark():
    num = 0
    while num < 10:
        time.sleep(1)
        print("计算时长 1 秒")
        num += 1


def long_fun():
    num = 0
    while num < 10000:
        math.factorial(num)
        num += 1


def longtime_fun():
    start_time = datetime.datetime.now()
    # 04_spark()
    long_fun()
    end_time = datetime.datetime.now()
    print("计算总时长 %d 秒" % (end_time - start_time).seconds)


if __name__ == '__main__':
    # sc = SparkContext("local", "first app")
    # longtime_fun()
    cmd_cpu = "ssh root@192.168.8.9 free -t"
    res = os.popen(cmd_cpu).readlines()
    print(res)
    ress = ' '.join(res[-1].split()).split(" ")
    print(' '.join(res[-1].split()).split(" "))
    print(int(ress[2])/int(ress[1])*100)
