# ！/usr/bin/python3
# -*- coding:utf-8 -*-


def nop():
    # 定义空函数
    pass


def check_args(x):
    # 参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')


"""递归函数
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，
这个函数就是递归函数
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def multi_result(x, y):
    # 返回多个结果（实质是返回tuple）
    return x, y


x, y = multi_result(1, 2)


def args_location(x, y):
    # 位置（必选）参数
    pass


def args_default(x, y=2):
    # 默认参数
    pass


def args_change(*args):
    # 可变参数  允许你传入 0 个或任意个参数
    # Python 允许你在 list 或 tuple,前面加一个*号，把 list 或 tuple 的元素变成可变参数传进去
    # 可变参数在函数调用时自动组装为一个 tuple
    for arg in args:
        pass


def args_kv(**kwargs):
    # 关键字参数 允许你传入 0 个或任意个含参数名的参数
    # 这些关键字参数在函数内部自动组装为一个 dict
    pass


args_kv(name1=1, name2=2)


def args_named(name, age, *, city, job):
    # 命名关键字参数 命名关键字参数需要一个特殊分隔符*， *后面的参数被视为命名关键字参数
    pass


args_named('Jack', 24, city='Beijing', job='Engineer')

"""参数组合
在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键
字参数和命名关键字参数，这 5 种参数都可以组合使用，除了可变参数
无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必
选参数、默认参数、可变参数/命名关键字参数和关键字参数。
"""
