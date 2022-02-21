# ！/usr/bin/python
# -*- coding:utf-8 -*-

"""模块注释：
    获取 sparksession
"""
from pyspark.sql import SparkSession


def get_spark_hive():
    spark = SparkSession.builder.master('local[*]') \
        .config('spark.executor.memory', '4g') \
        .config('spark.driver.memory', '4g') \
        .config('hive.metastore.uris', 'thrift://%s:9083' % '192.168.43.70') \
        .enableHiveSupport() \
        .appName('spark_app_name') \
        .getOrCreate()
    return spark


def get_spark_local():
    spark = SparkSession.builder.master('local[*]') \
        .config('spark.executor.memory', '4g') \
        .config('spark.driver.memory', '4g') \
        .appName('spark_app_name') \
        .getOrCreate()
    return spark
