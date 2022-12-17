# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
获取服务器资源
"""

__author__ = 'HOU'

import psutil
import pymysql


def get_server_info():
    """方法注释：
    内存使用情况，磁盘使用情况，CPU 使用情况
    """
    # 内存使用情况
    server_memory = psutil.virtual_memory()[2]
    # 磁盘使用情况
    server_disk = psutil.disk_partitions()
    # 'C:\\'
    server_disk_usage = psutil.disk_usage('/')[3]
    # CPU 使用情况
    # for x in range(10):
    server_cpu = psutil.cpu_percent(interval=1, percpu=True)

    server_dict = {'server_memory': server_memory, 'server_disk_usage': server_disk_usage, 'server_cpu': server_cpu}
    return server_dict


def select_data1():
    # 打开数据库连接
    db = pymysql.connect(host='192.168.43.61', port=3306, user='root', password='314315', db='basedb',
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM sys_config")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    return data

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    get_server_info()
