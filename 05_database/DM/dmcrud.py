# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-01-01
模块注释：
"""
# coding: utf-8
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker
from model import Product


def main():
    # dialect 是SQLAlchemy用来与各种类型的DBAPI和数据库通信的系统。
    conn_url = 'dm+dmPython://SYSDBA:SYSDBA@127.0.0.1:5236?schema=test'
    # 创建Engine对象
    engine = create_engine(conn_url,echo=True)
    with engine.connect() as con:
        rs = con.execute(('select 1 from dual'))
        print(f"连接-达梦数据库:-成功!" if rs.rowcount == 1 else f"连接-达梦数据库:-失败！")
    # 创建DBSession对象
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    statement = select(Product)
    list_product = session.execute(statement).scalars().all()
    print(list_product)
    # fun_select_all(DBSession)
    # # 插入
    # fun_insert(DBSession)
    # fun_select_all(DBSession)
    # # 更新
    # fun_update(DBSession)
    # fun_select_all(DBSession)
    # # 删除
    # fun_delete(DBSession)
    # fun_select_all(DBSession)


def dmpython_test():
    import dmPython
    conn = dmPython.connect(user='SYSDBA', password='SYSDBA', server='127.0.0.1', port=5236)
    cursor = conn.cursor()
    sql = 'select 1 from dual'
    cursor.execute(sql)
    value = cursor.fetchall()
    print(value)


if __name__ == '__main__':
    # dmpython_test()
    main()
