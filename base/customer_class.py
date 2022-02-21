# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    定制类
    __slots__:限制类属性 __slots__ = ('__name', 'score')
    __str__：打印实例
    __repr__:为调试服务的,打印实例
    __iter__:迭代对象
    __getitem__:像 list 那样按照下标取出元素
    __getattr__ :
    __call__:对实例进行调用
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'my name is %s' % self.name

    __repr__ = __str__

    def __call__(self):
        print('my name is %s' % self.name)


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a = self.b
        self.b = self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a = 1
        b = 1
        if isinstance(item, int):
            for n in range(item):
                a = b
                b = a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            L = []
            for n in range(stop):
                if n >= start:
                    L.append(a)
                a, b = b, a + b
            return L


if __name__ == '__main__':
    import pandas as pd
    s = Student('HOU')
    s.age = pd.DataFrame()
    s1 = Student('HXT')
    L = []
    L.append(s)
    L.append(s1)


    for n in Fib():
        print(n)

    s()
