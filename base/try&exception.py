# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
flask框架例子
"""
__author__ = "HOU"


def f(x):
    assert x < 0, 'x must be negative'  # 断言
    return x * 2


def f1(x):
    ex = '异常'
    if x > 0:
        raise ex  # 错误上抛
    return x * 2


if __name__ == '__main__':
    try:
        print(f1(5))
    except Exception as ex:
        print(ex)
    finally:
        print('finally')

    # with as 退出是必须执行
    # 符合环境管理协议的 对象可以使用 with as（对象必须包含__enter__和 __exit__ 方法     ）


