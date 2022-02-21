# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

import get_spark as spark_session
import sqlalchemy
import pyhive

if __name__ == '__main__':
    spark = spark_session.get_spark_local()
    df = spark.read.csv('data.csv', header='true', inferSchema='true', sep='\t')
    df.show(30)