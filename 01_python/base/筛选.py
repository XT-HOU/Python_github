# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    干什么用的
"""
__author__ = "HOU"

from random import randint

if __name__ == '__main__':
    list1 = [randint(-10, 10) for x in range(15)]
    res = [one for one in list1 if one >= 0]
    print(res)

    d1 = {k: randint(60, 100) for k in range(1, 21)}
    d2 = {k: v for k, v in d1.items() if v > 90}
    print(d2)