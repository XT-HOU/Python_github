# ！/usr/bin/python
# -*- coding:utf-8 -*-

"""模块注释：
    干什么用的
"""
from pyspark import SparkContext

sc = SparkContext("local", "first app")
print("Lines with a: %d, lines with b: %d" % (1, 2))
