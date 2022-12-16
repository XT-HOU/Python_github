# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    04_spark 操作
"""
__author__ = "HOU"

from pyspark.sql import SparkSession
import socket
import target_params


def get_spark():
    """方法注释：
        获取 SparkSession, 判断是否是集群返回不同 SparkSession
    :return: SparkSession
    """
    target_name = 'target_name'
    name, ip = get_ip()
    ip_service = ('192.168.0.135', '')

    if target_params.params.get('target_name') is not None:
        target_name = target_params['target_name']
#
    if not ip_service.__contains__(ip):
        spark_single = SparkSession.builder.master("local[*]")\
            .config("04_spark.executor.memory", "4g")\
            .config("04_spark.dirver.memory", "4g")\
            .config("03_hive.metastore.uris", "thrift://192.168.43.70:9083")\
            .enableHiveSupport()\
            .appName(target_name)\
            .getOrCreate()
    else:
        spark_single = SparkSession.builder.appName(target_name).getOrCreate()

    return spark_single


def get_ip():
    """方法注释：
        获取本机 name 和 ip
    :return:name,ip
    """
    name = socket.getfqdn(socket.gethostname())
    ip = socket.gethostbyname(name)
    return name, ip


def spark_data_frame():
    spark = get_spark()
    sc = spark.sparkContext
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
    rdd = sc.parallelize(a)
    df = spark.read.json(rdd)
    df.show()
    res = df.where((df.速度 >= 0) & (df.速度<=60)).orderBy(df.速度, ascending=False).collect()
    result = [one for one in res if one.速度 <= '50']
    print(result)
    ret = result.sort(key=lambda x: float(x.速度), reverse=False)
    print(result)
    result.sort(key=lambda x: float(x.速度), reverse=True)
    print(result)
    # print(res.first().time)
    # for item in res:
    #     print(item.time.value)
    print(1)


def ji_fen():
    from scipy import integrate

    def fun(v, t):
        return v * t

    v, err = integrate.quad(fun, 1, 5, args=5)
    print(v, err)


def time_change():
    import time, datetime
    tss1 = '00:00:00.966888'
    timeArray = time.strptime(tss1, "%H:%M:%S.%f")
    tupleTime = datetime.datetime.strptime(tss1, "%H:%M:%S.%f")
    timp = float(time.mktime(tupleTime.timetuple())) + (tupleTime.microsecond * 0.000001)
    print(timp)


class Person(object):
    def __init__(self,name=None):
        self.name = name


if __name__ == '__main__':
    spark_single = SparkSession.builder.appName("app").getOrCreate()

    spark = get_spark()
    sql = "select * from default.demo01 "
    df = spark.sql(sql)
    print(df.collect())
import pyspark.str

