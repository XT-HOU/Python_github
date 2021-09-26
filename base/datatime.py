# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

if __name__ == '__main__':
    from datetime import datetime
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # '2016-07-21 19:49:15'
    print(datetime.now().isoformat())
    # '2016-07-21T19:56:46.744893'
    print(str(datetime.now()))
    # '2016-07-21 19:48:37.436886'
