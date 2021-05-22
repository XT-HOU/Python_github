# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    主方法
"""
__author__ = "HOU"

import psutil


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
    if isinstance(server_cpu, list):
        cpu_all = 0
        for item in server_cpu:
            cpu_all += item
        cpu_avg = round(cpu_all/len(server_cpu), 2)
        server_dict = {'server_memory': server_memory, 'server_disk_usage': server_disk_usage, 'server_cpu': cpu_avg}
        return server_dict



