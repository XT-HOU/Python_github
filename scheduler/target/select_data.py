# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    查询数据脚本
"""
__author__ = "HOU"
import pymysql


def select_data():
    return {}


def select_data1():
    # 打开数据库连接
    db = pymysql.connect(host='192.168.8.9', port=3306, user='root', password='314315', db='analysisdb',
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM USER")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    print(data)

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    select_data1()