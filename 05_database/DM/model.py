# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
"""
# coding: utf-8
from sqlalchemy import Column, Integer, String,Date,Numeric,Text
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

class Product(Base):
    # 表的名字:
    __tablename__ = 'product'
    # 表的结构:
    PRODUCTID = Column(Integer,autoincrement=True, primary_key=True)
    NAME = Column(String(100))
    AUTHOR = Column(String(25))
    PUBLISHER = Column(String(50))
    PUBLISHTIME = Column(Date)
