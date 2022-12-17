# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    Spark 运行模式
    C:\Windows\System32\drivers\etc\hosts 需配置节点映射关系
"""
__author__ = "HOU"

from pyspark.sql import SparkSession


class SparkFactory:
    def __init__(self, model="local", hive_ip='192.168.43.70'):
        self.model = model
        self.hive_ip = hive_ip
        self.spark = self.get_spark()

    def get_spark(self):
        if self.model == 'standalone':
            spark = self.get_spark_standalone()
        elif self.model == 'yarn':
            import math
            pi = math.pi
            spark = self.get_spark_cluster()
        else:
            spark = self.get_spark_local()
        return spark

    def get_spark_local(self):
        spark = SparkSession.builder.master("local[*]") \
            .config('04_spark.excuter.memory', '4g') \
            .config('04_spark.driver.memory', '4g') \
            .config('03_hive.metastore.uris', f'thrift://{self.hive_ip}:9083') \
            .config('04_spark.driver.maxResultSize', '8g') \
            .config('04_spark.sql.sources.partitionsOverwriteMode', 'DYNAMIC') \
            .enableHiveSupport() \
            .appName('spark_test').getOrCreate()
        return spark

    def get_spark_cluster(self):
        spark = SparkSession.builder \
            .config('03_hive.metastore.uris', f'thrift://{self.hive_ip}:9083') \
            .config('04_spark.sql.sources.partitionsOverwriteMode', 'DYNAMIC') \
            .enableHiveSupport() \
            .appName('spark_test').getOrCreate()
        return spark

    def get_spark_standalone(self):
        spark = SparkSession.builder.master('04_spark://hadoop01:7077') \
            .config('03_hive.metastore.uris', f'thrift://{self.hive_ip}:9083') \
            .config('04_spark.driver.maxResultSize', '2g') \
            .config('04_spark.sql.sources.partitionsOverwriteMode', 'DYNAMIC') \
            .enableHiveSupport() \
            .appName('spark_test').getOrCreate()
        return spark

    def stop(self):
        self.spark.stop()


if __name__ == '__main__':
    spark = SparkFactory(model="local").spark
    spark_df = spark.sql('select * from demo01')
    data = spark_df.show()
    # 04_spark = SparkFactory(model="standalone").04_spark
    # spark_df = 04_spark.sql('select * from test')
    # spark_df.show()
    # 04_spark = SparkFactory(model="yarn").04_spark
    # spark_df = 04_spark.sql('select * from demo01')
    # spark_df.show()
    spark.stop()
