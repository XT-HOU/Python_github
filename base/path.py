# ！/usr/bin/python3
# -*- coding:utf-8 -*-

import os

print('1123'.replace('1',''))

print("===获取当前文件目录===")
# 当前脚本工作的目录路径
print(os.getcwd())
# os.path.abspath()获得绝对路径
print(os.path.abspath(os.path.dirname(__file__)))

print("=== 获取当前文件上层目录 ===")
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))
print(os.path.dirname(os.getcwd()))
# os.path.join()连接目录名与文件或目录


print("==== 设置路径为当前文件上层目录的test_case文件夹====")
path = os.path.join(os.path.dirname(os.getcwd()), "test_case")
print(path)
