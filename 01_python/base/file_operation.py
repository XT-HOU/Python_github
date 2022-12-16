# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    1.异步读写文件
    2.文件内容多空格合并
"""

import asyncio
import os
import aiofiles
import datetime


async def wirte_demo():
    """
        异步方式写入文件
    """
    # 异步方式执行with操作,修改为 async with
    async with aiofiles.open("/io/text.txt", "w", encoding="utf-8") as fp:
        await fp.write("hello world ")
        print("数据写入成功")


async def read_demo():
    """
        异步方式读取文件全部内容
    """
    async with aiofiles.open("/io/resource.txt", "r", encoding="utf-8") as fp:
        # 读取全部
        content = await fp.read()
        print(content)


async def read2_demo():
    """
        异步方式按行读取文件
    """
    async with aiofiles.open("/io/text.txt", "r", encoding="utf-8") as fp:
        # 读取每行
        async for line in fp:
            print(line)


async def test():
    """
        异步方式读取文件并写入文件
    """
    async with aiofiles.open('/io/resource.txt', "r", encoding="utf-8") as fp:
        # 读取每行
        async for line in fp.read():
            async with aiofiles.open("/io/aa.txt", "a", encoding="utf-8") as f:
                await f.write(line)
                # print(line)


def union_space():
    """
        将文件中的多个空格合并为一个
    :return:
    """

    filePath = '/io/deal/'
    # 读取路径下的所有文件及文件夹
    listdir = os.listdir(filePath)

    for name in listdir:
        path = os.path.join(filePath, name)
        if not os.path.isdir(path):
            with open(filePath + name) as f:
                for line in f.readlines():
                    with open(filePath + 'deal/' + name, 'a') as m:
                        m.writelines(' '.join(line.split()))
                        m.write('\n')


if __name__ == "__main__":
    print(datetime.datetime.now())
    # asyncio.run(wirte_demo())
    # asyncio.run(read_demo())
    asyncio.run(test())
    print(datetime.datetime.now())
