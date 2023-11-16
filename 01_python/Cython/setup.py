# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
    目录小不要有 init 文件
    转换文件命令 python setup.py build_ext --inplace
"""
from distutils.core import setup
from Cython.Build import cythonize

setup(name='hello',
      ext_modules=cythonize("hello.py"))