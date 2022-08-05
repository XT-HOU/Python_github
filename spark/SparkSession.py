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
            spark = self.get_spark_cluster()
        else:
            spark = self.get_spark_local()
        return spark

    def get_spark_local(self):
        spark = SparkSession.builder.master("local[*]") \
            .config('spark.excuter.memory', '4g') \
            .config('spark.driver.memory', '4g') \
            .config('hive.metastore.uris', f'thrift://{self.hive_ip}:9083') \
            .config('spark.driver.maxResultSize', '8g') \
            .config('spark.sql.sources.partitionsOverwriteMode', 'DYNAMIC') \
            .enableHiveSupport() \
            .appName('spark_test').getOrCreate()
        return spark

    def get_spark_cluster(self):
        spark = SparkSession.builder \
            .config('hive.metastore.uris', f'thrift://{self.hive_ip}:9083') \
            .config('spark.sql.sources.partitionsOverwriteMode', 'DYNAMIC') \
            .enableHiveSupport() \
            .appName('spark_test').getOrCreate()
        return spark

    def get_spark_standalone(self):
        spark = SparkSession.builder.master('spark://hadoop01:7077') \
            .config('hive.metastore.uris', f'thrift://{self.hive_ip}:9083') \
            .config('spark.driver.maxResultSize', '2g') \
            .config('spark.sql.sources.partitionsOverwriteMode', 'DYNAMIC') \
            .enableHiveSupport() \
            .appName('spark_test').getOrCreate()
        return spark

    def stop(self):
        self.spark.stop()


if __name__ == '__main__':
    spark = SparkFactory(model="local").spark
    spark_df = spark.sql('select * from demo01')
    data = spark_df.show()
    # spark = SparkFactory(model="standalone").spark
    # spark_df = spark.sql('select * from test')
    # spark_df.show()
    # spark = SparkFactory(model="yarn").spark
    # spark_df = spark.sql('select * from demo01')
    # spark_df.show()
    spark.stop()
