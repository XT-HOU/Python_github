# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"


class Test:
    def __init__(self):
        print('Test id is %d' % id(self))


if __name__ == '__main__':
    str = 'total:  34635    34354    3545465'
    print(' '.join(str.split()).split(' ')[2])

