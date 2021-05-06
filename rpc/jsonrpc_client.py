# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# JSON-RPC server needing 'pip install jsonrpclib-pelix'

from jsonrpclib import Server


def main():
    proxy = Server('http://127.0.0.1:7000')
    print(proxy.length((123, 465)))


if __name__ == '__main__':
    main()
