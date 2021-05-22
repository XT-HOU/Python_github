# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    常用常量枚举
"""
__author__ = "HOU"

from enum import Enum, unique


@unique
class Default(Enum):
    APP_LIST_LEN = 100
    '''编排提交上限'''
    MSG_LEN = "达到提交上限：%d" % APP_LIST_LEN
    OK = 'OK'
    PUBLIC_APP = '0'
    '''公共空间'''
    PRIVATE_APP = '1'
    '''个人空间'''
    OS_WINDOWS = "Windows"
    '''Windows 操作系统'''
    OS_LINUX = "Linux"
    '''Linux 操作系统'''


@unique
class AppState(Enum):
    APP_STATE0 = '0'
    '''编排状态0：正常提交 1：暂停'''
    APP_STATE1 = '1'
    '''编排状态0：正常提交 1：暂停'''


@unique
class ScriptType(Enum):
    SCRIPT_PYTHON = 'python3'
    '''python3 脚本'''
    SCRIPT_JAVA = 'java'
    '''Java 脚本'''
    SCRIPT_MATLAB = 'matlab'
    '''MATLAB 脚本'''


if __name__ == '__main__':
    print(Default.APP_LIST_LEN.value)
    action_sort = [1, 6, 9, 0]
    action_sort.sort(key=lambda x: x)
    print(action_sort)