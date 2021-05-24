# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    面向对象用法总结
"""
import json

"""访问限制：
    在 Python 中，实例的变量名如果以__开头，就变成了一个私有变量（ private），只有内部可以访问，外部不能访问
    在Python中，通过单下划线”_”来实现模块级别的私有化，一般约定以单下划线”_”开头的变量、函数为模块私有的，
也就是说”from moduleName import *”将不会引入以单下划线”_”开头的变量、函数;
“__”：双下划线的表示的是private类型的变量。只能是允许这个类本身进行访问了，连子类也不可以，这类属性在运行时属性名会加上单下划线和类名。
    在 Python 中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访
问的，不是 private 变量，所以，不能用__name__、 __score__这样的变量名。
    有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到
这样的变量时，意思就是， “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

单前导下划线 _var
    当涉及到变量和方法名称时，单个下划线前缀有一个约定俗成的含义。 下划线前缀的含义是告知其他程序员：以单个下划线开头的变量或方法仅供内部使用。 该约定在PEP 8中有定义。这不是Python强制规定的。 Python不像Java那样在“私有”和“公共”变量之间有很强的区别。 
单末尾下划线 var_
    有时候，一个变量的最合适的名称已经被一个关键字所占用。 因此，像class或def这样的名称不能用作Python中的变量名称。 在这种情况下，你可以附加一个下划线来解决命名冲突
双前导下划线 __var
    双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。这也叫做名称修饰（name mangling） - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
双前导和双末尾下划线 _var_
    魔法方法。Python保留了有双前导和双末尾下划线的名称，用于特殊用途。 这样的例子有，__init__对象构造函数，或__call__ --- 它使得一个对象可以被调用。
单下划线 _
    按照习惯，有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的。
"""


# 新建类类名首字母大写
class Student(object):
    # __slots__ = ('__name', 'score')

    # 初始化，私有函数
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.score))


s = Student('hou', 99)
print(s.__dict__)
print(json.dumps(s, default=lambda x: x.__dict__))
s.print_score()
"""继承：
    当子类和父类都存在相同的 run()方法时，我们说，子类的 run()覆盖了父类的 run()，在代码运行的时候，总是会调用子类的 run()。
"""
print(isinstance((1, 2, 3), (list, tuple)))

"""反射：
    如果要获得一个对象的所有属性和方法，可以使用 dir()函数，它返回一个包含字符串的 list
类似__xxx__的属性和方法在 Python 中都是有特殊用途的,仅仅把属性和方法列出来是不够的，配合 getattr()、 setattr()以及
hasattr()，我们可以直接操作一个对象的状态
"""
print(dir('abc'))

"""使用 __slots__：
    Python 允许在定义 class 的时候，定义一个特殊的__slots__变量，来限制该 class 实例能添加的属性
使用__slots__要注意， __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
"""
s.age = 88

"""使用 get/set：
    Python 允许在定义 class 的时候，定义一个特殊的__slots__变量，来限制该 class 实例能添加的属性
使用__slots__要注意， __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
"""


class People(object):
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2021 - self.__birth


"""多继承：
    在设计类的继承关系时，通常，主线都是单一继承下来的，例如， Ostrich 继承自 Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。这
种设计通常称之为 MixIn。
"""
