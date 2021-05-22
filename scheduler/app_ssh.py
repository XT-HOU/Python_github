# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    python实现ssh功能
"""
__author__ = "HOU"

# import paramiko
import os
from default import ScriptType
from globals import ssh_list

# windows 下是否开启远程连接
global open_shell
open_shell = False


# def start_ssh():
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname='192.168.8.9', port=22, username='root', password='314315')
#     ssh_list.append(ssh)
#     global open_shell
#     open_shell = True
#     print('连接%s成功' % ssh.get_host_keys())


def send_cmd_windows(script_type, path, filename):
    """方法注释：
        Windows下发送shell命令
        'python3 /usr/python/spark_python_test.py'
        'ls -l;ifconfig' 多个命令用;隔开
    :param script_type:
    :param path: 脚本路径
    :param filename: 脚本文件名
    """
    if not open_shell:
        # start_ssh()
        pass
    cmd = ''
    if script_type == ScriptType.SCRIPT_PYTHON.value:
        cmd = 'python3 %s/%s' % (path, filename)
    elif script_type == ScriptType.SCRIPT_JAVA.value:
        cmd = "暂不支持Java"
    stdin, stdout, stderr = ssh_list[0].exec_command(cmd)
    print(cmd)
    # 接收输出或错误信息
    # result = stdout.read()
    # if not result:
    #     result = stderr.read()
    # print(result.decode())


def send_cmd_linux(script_type, path, filename):
    """ 方法注释：
        Linux 下免密发送 shell 命令
        ssh root@192.168.8.9 "ls -l"
        'ls -l;ifconfig' 多个命令用;隔开
    :param script_type:
    :param path: 脚本路径
    :param filename: 脚本文件名
    """
    cmd = ''
    if script_type == ScriptType.SCRIPT_PYTHON.value:
        cmd = 'ssh root@192.168.8.9 "python3 %s/%s"' % (path, filename)
    elif script_type == ScriptType.SCRIPT_JAVA.value:
        cmd = "暂不支持Java"
    os.system(cmd)
    print(cmd)


# def close():
#     """方法注释：
#         关闭 ssh 连接
#     """
#     for ssh in ssh_list:
#         ssh.close()
#     ssh_list.clear()


if __name__ == '__main__':
    pass
