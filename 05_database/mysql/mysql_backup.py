# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
mysql数据库备份与还原
    1.检查运行程序的电脑是否安装了mysql
    2.是否可以执行 mysqldump cmd命令
"""
__author__ = "HOU"

import os
import time
import schedule

# 需要备份的数据库
databases = ['f725e8227263f15e', 'f725230448eb1b5b']
# 数据库地址
db_host = '192.168.43.8'
db_username = 'root'
db_pwd = '314315'
# 存放备份地址
backup_path = './mysql_db_backup/'


def back_up():
    """方法注释：
        数据全量备份
    :return:
    """
    dir_path = backup_path + time.strftime('%Y%m%d') + "/"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    print('make directory success:', os.path.abspath(dir_path))
    # 改变当前工作目录到指定的路径
    os.chdir(dir_path)
    for database_name in databases:  # 循环要备份的数据库
        today_sql = database_name + '_' + time.strftime('%Y%m%d') + '.sql'  # 定义数据库备份的文件名
        # 编写cmd语句， 定义备份数据库备份命令
        sql_comm = f"mysqldump --skip-opt -h{db_host} -u{db_username} -p{db_pwd} -B {database_name}  " \
                   f"--max_allowed_packet=1073742824 --default_character-set=utf8 > {today_sql} "
        if os.system(sql_comm) == 0:  # 如果上一条执行结果等于0，表示成功
            print(database_name, 'is backup success!')  # 打印成功信息
            print('备份文件地址:', os.path.abspath(dir_path) + '/' + today_sql)
        else:  # 备份失败
            print(database_name, 'is backup fail!')  # 打印成功信息


def reduction():
    """方法注释：
        数据还原
    :return:
    """
    # --还原数据库（远程还原速度慢）
    # mysql - h192.168.0.137 - p3306 - -default - character - set = utf8 - -max_allowed_packet = 1073742824 - uroot - p123456 < all.sql
    # --连接超时（要导入的mysqldump文件中insert的values值太多，超过了MySQL参数max_allowed_packet的值，进而导致导入操作中断退出。）
    # mysql > set
    # global max_allowed_packet=67108864;
    # --source
    # 还原数据库(速度快，需远程数据库电脑)
    # mysql > source
    # D:\dbname1.sql


def job():
    """方法注释：
        定时执行
    :return:
    """
    # 设置执行条件
    schedule.every().day.at("00:30").do(back_up)
    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == '__main__':
    # todo 添加获取数据库版本,还原需数据库版本一致等条件
    # 检查运行程序的电脑是否安装了mysql
    job()
