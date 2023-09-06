# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
@author: hou
@time: 2023-07-01
模块注释：
    SQLAlchemy,基本功能

"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)
    country = Column(String(50))


def engine_mysql():
    # 准备连接数据库基本信息
    # 代表哪一台计算机，ip地址是多少
    HOSTNAME = '192.168.43.8'
    # 端口号
    PORT = '3306'
    # 数据库的名字，连接那个数据库
    DATABASE = 'test'
    # 数据库的账号和密码
    USERNAME = 'root'
    PASSWORD = '314315'
    # 创建数据库引擎
    # engine = create_engine(DB_URI, echo=True)
    engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}?charset=utf8",
                           echo=True,  # 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
                           pool_size=8,  # 连接池的大小，默认为5个，设置为0时表示连接无限制
                           pool_recycle=60 * 30  # 设置时间以限制数据库多久没连接自动断开
                           )
    # 使用with语句连接数据库，如果发生异常会被捕获
    with engine.connect() as con:
        rs = con.execute(text('SELECT 1'))
        print("连接成功!" if rs.rowcount == 1 else "连接失败！")
    return engine


def init_db(engine):
    # 注意点：一旦使用`Base.metadata.create_all()`将模型映射到数据库中后，即使改变了模型的字段，也不会重新映射了。
    # 解决方法：先将表全部删除之后再创建新的表
    # 将Base上的ORM类模型对应的数据表都删除
    # Base.metadata.drop_all()
    # 创建Base上的ORM类到数据库中成为表
    Base.metadata.create_all(engine)
    pass


if __name__ == '__main__':
    engine = engine_mysql()
    # sqlalchemy中使用session用于创建程序和数据库之间的会话，所有对象的载入和保存都需要通过session对象 。
    # 创建session
    # session的常见操作方法包括：
    # flush：预提交，提交到数据库文件，还未写入数据库文件中(没事用)
    # commit：提交了一个事务
    # rollback：回滚
    # close：关闭
    DbSession = sessionmaker(bind=engine)
    session = DbSession()
    init_db(engine)
    person = Person(name="123")
    session.add(person)
    session.commit()
    ps = session.query(Person).all()
    session.close()
