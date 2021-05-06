# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# JSON-RPC server needing 'pip install jsonrpclib-pelix'

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def length(*args):
    """ 计算每个参数长度
    :param args:
    :return:
    """
    result = []
    for arg in args:
        try:
            arg_len = len(arg)
        except TypeError:
            arg_len = None
        result.append(arg_len)
    return result


def main():
    server = SimpleJSONRPCServer(('127.0.0.1', 7000))
    server.register_function(length)
    print('Staring server ......')
    server.serve_forever()


if __name__ == '__main__':
    main()
