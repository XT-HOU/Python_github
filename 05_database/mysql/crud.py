# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    mysql CRUD
"""
import pymysql


def select_data1():
    """ 方法注释：
        查询数据
    """

    # 打开数据库连接
    db = pymysql.connect(host='192.168.43.61', port=3306, user='root', password='314315', db='basedb',
                         charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM sys_config")

    # 使用 fetchone() 方法获取单条数据.
    # todo
    data = cursor.fetchall()

    return data

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    select_data1()
