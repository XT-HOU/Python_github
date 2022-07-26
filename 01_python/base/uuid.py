# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    UUID是指一台机器上生成的数字，他保证同一时空所有机器都是唯一的。
    UUID由以下几部分构成：
　　　　（1）时间戳：根据当前时间或者时钟序列生成字符串
　　　　（2）全剧唯一的机器识别号，根据网卡MAC地址或者IP获取，如果没有网卡则以其他方式获取。
　　　　（3）随机数：机器自动随机一组序列

uuid有5种生成算法，分别是uuid1()、uuid2()、uuid3()、uuid4()、uuid5()。

　　1、uuid1（）基于时间戳
　　　　由MAC地址、当前时间戳、随机数字。保证全球范围内的唯一性。但是由于MAC地址使用会带来安全问题，局域网内使用IP代替MAC
　　2、uuid2() 基于分布式环境DCE
　　　　算法和uuid1相同，不同的是把时间戳前四位换成POIX的UID，实际很少使用。注意：python中没有这个函数
　　3、uuid3() 基于名字和MD5散列值
　　　　通过计算名字和命名空间的MD5散列值得到的，保证了同一命名空间中不同名字的唯一性，不同命名空间的唯一性。但是同一命名空间相同名字生成相同的uuid。
　　4、uuid4() 基于随机数
　　　　由伪随机数得到的，有一定重复概率，这个概率是可以算出来的
　　5、uuid5() 基于名字和SAHI值
　　　　算法和uuid3相同，不同的是使用SAHI算法

使用经验：
　　1、由于python中没有DCE，所以uuid2()可以忽略
　　2、uuid4()存在概率重复性，由于无映射性，最好不使用
　　3、如果是全局的分布式环境下，最好使用uuid1()
　　4、若名字的唯一性要求，最好使用uuid3()或者uuid5()
"""
__author__ = "HOU"
import uuid
import time

if __name__ == '__main__':
    # uuid1 = uuid.uuid1()
    # print(str(uuid1).replace('-', ''))
    print(tuple(eval("(1,2,3)")))
    import random

    num = 20
    while num > 0:
        num -= 1
        print(round(random.uniform(260, 330),1))

    num = 20
    while num > 0:
        num -= 1
        a1 = (2021, 5, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
        a2 = (2021, 8, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d %H:%M", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        print( date)
