# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    枚举类型
"""
from enum import Enum, unique


@unique
class Weekday(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WEN = 3
    THU = 4
    FRI = 5
    SAT = 6


if __name__ == '__main__':
    # Weekday.SUN = 7
    print(Weekday.SUN)
    print(Weekday.SUN.value)
