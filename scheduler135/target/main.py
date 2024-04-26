# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    定义函数执行顺序
    TODO：考虑自定义算子如何执行，按设计图顺序动态生成脚本
"""
__author__ = "HOU"

import target_data
import result_data
import algorithm
import target_params
import datetime


def main():
    """方法注释：
        指标模型执行顺序
    :return:
    """
    target_params.get_params()
    # 获取多个数据
    target_data.add_data()
    algorithm.target_caluate()
    #
    result_data.insert_data()


def run():
    """方法注释：
        提交spark
    :return:
    """
    start_time = datetime.datetime.now()
    print("---------------------start----------------------")
    main()
    end_time = datetime.datetime.now()
    print("total_time: %d sec" % (end_time - start_time).seconds)
    print("---------------------end----------------------")


if __name__ == '__main__':
    try:
        run()
    except Exception as ret:
        target_params.logger.error(ret)
    finally:
        target_params.spark.stop()
