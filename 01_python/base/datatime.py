# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"

import time
from datetime import datetime


def unix_time_micro(str_dt):
    """方法注释：
        返回unix时间
    :param str_dt: 时间字符串 例：2020-09-01 20:00:34.050
    :return: 毫秒数
    """
    # 转换成时间数组
    timeArray = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S.%f")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray.timetuple()) * 1000 + timeArray.microsecond / 1000)
    return timestamp


def unix_time_sec(str_dt):
    """方法注释：
        返回unix时间
    :param str_dt: 时间字符串 例：2020-09-01 20:00:34.050
    :return: 秒数
    """
    # 转换成时间数组
    timeArray = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S.%f")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray.timetuple()))
    return timestamp


def time_test():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    # '2016-07-21 19:49:15'
    print(datetime.now().isoformat())
    # '2016-07-21T19:56:46.744893'
    print(str(datetime.now()))
    # '2016-07-21 19:48:37.436886'
    d_time = datetime.strptime('23:59:59.258', '%H:%M:%S.%f')
    print((d_time + dt.timedelta(seconds=1)))
    r = int(time.mktime(datetime.now().timetuple()))
    print(r)
    timestr = '1971-01-01'
    datetime_obj = datetime.strptime(timestr, "%Y-%m-%d")
    obj_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    print(obj_stamp)


if __name__ == '__main__':
    from datetime import datetime
    import datetime as dt

    aa = unix_time_sec("2020-09-01 20:00:34.050")
    # aa = (datetime.utcnow() - datetime(1970, 1, 1)).microseconds
    print(aa)
    # time_test()
