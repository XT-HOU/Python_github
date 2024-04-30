# ！/usr/bin/python3
# -*- coding:utf-8 -*-


import sys
import psutil

# 当前脚本工作的目录路径 os.getcwd() cmd运行获取的是cmd路径
sys.path.append('D:\PythonCode\PythonExplore')


def all_unique(lst):
    # 去除重复元素
    return set(lst)


def get_sizeof_obj(obj):
    # 获取对象内存使用大小
    return sys.getsizeof(obj)


def get_computer_info():
    # 内存使用情况
    print(psutil.virtual_memory())
    # 磁盘使用情况
    print(psutil.disk_partitions())
    # 'C:\\'
    print(psutil.disk_usage('/'))
    # CPU 使用情况
    for x in range(10):
        print(psutil.cpu_percent(interval=1, percpu=True))


if __name__ == '__main__':
    get_computer_info()
