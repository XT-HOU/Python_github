# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    python 基础数据类型
    number,string,bool,list,tuple,set,dictionary
"""
__author__ = "HOU"


def number_demo():
    # Python 支持三种不同的数值类型,int,float,complex
    # Python3 int,float是没有限制大小的
    # 复数（complex）由实数部分和虚数部分构成，可以用a+bj 或者 complex(a,b)表示，复数的实部a和虚部b都是虚数
    # 其它进制的整数，二进制以0b开头，八进制以0o开头，十六进制以0x开头
    # 类型转换
    print(int('2'))
    print(float('3.3'))


def string_demo():
    # 字符串创建
    str1 = 'China'
    str2 = "China"
    # 字符串截取 变量[头下标:尾下标]
    print(str1[0:1])
    # 转义字符 \
    # 格式化字符串
    print("123" + "456")  # 类型必须一致
    print("123", 465)  # 自带空格
    # %s:字符串，%d:有符号的十进制整数（%0nd:0-位数不够用0代替，n-位数），%f:有符号的十进制浮点数（%.nf:.-代表小数点，n-代表小数位数）
    print("姓名：%s,学号：%03d,成绩：%.2f" % (str2, -123, -99.5))
    # f格式化字符串（推荐使用）
    print(f"国籍：{str1},姓名：{'hxt'}")
    pass


def list_demo():
    # 创建[]
    names = ["张三", "李四", "王五", "赵六", "田七"]
    # 切片 [起始位置：结束位置：步长]
    print(names[-2:-1])
    print(names[1:4:2])
    # 操作
    # list.append(元素)，list.insert(下标，元素)，list.pop(下标)，list.remove(元素)，list.count(元素),list.reverse()
    pass


def tuple_demo():
    # tuple元组是一个不可变的序列
    names = ("张三", "李四", "王五", "赵六", "田七")
    # 用法同list


def set_demo():
    # set是一个不可重复的集合
    names = {"张三", "李四", "王五", "赵六", "张三"}
    print(names)
    # 用法同list


def dict_demo():
    # 创建
    name_dict = {1: "zhangsan", 2: "lisi"}
    # 添加或修改：dict[key]=123,删除：dict.pop(key),获取keys:dict.keys(),获取values：dict.values(),获取键值对：dict.items()
    name_dict[3] = "123"
    print(name_dict)
    pass


if __name__ == "__main__":
    dict_demo()
