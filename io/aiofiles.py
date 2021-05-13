# ！/usr/bin/python3
# -*- coding:utf-8 -*-

import asyncio
import aiofiles
import datetime


async def wirte_demo():
    # 异步方式执行with操作,修改为 async with
    async with aiofiles.open("/io/text.txt", "w", encoding="utf-8") as fp:
        await fp.write("hello world ")
        print("数据写入成功")


async def read_demo():
    async with aiofiles.open("/io/resource.txt", "r", encoding="utf-8") as fp:
        content = await fp.read()
        print(content)


async def read2_demo():
    async with aiofiles.open("/io/text.txt", "r", encoding="utf-8") as fp:
        # 读取每行
        async for line in fp:
            print(line)


async def test():
    async with aiofiles.open('/io/resource.txt', "r", encoding="utf-8") as fp:
        # 读取每行
        async for line in fp.read():
            async with aiofiles.open("/io/aa.txt", "a", encoding="utf-8") as f:
                await f.write(line)
                # print(line)


if __name__ == "__main__":
    print(datetime.datetime.now())
    # asyncio.run(wirte_demo())
    # asyncio.run(read_demo())
    asyncio.run(test())
    print(datetime.datetime.now())
