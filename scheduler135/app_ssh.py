# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    python实现ssh功能
"""
__author__ = "HOU"

import paramiko
import os
from default import ScriptType, Default
from globals import ssh_list, os_type, os_name, logger, global_dict, host_master
from spark_submit import get_cmd


def start_ssh():
    try:
        ssh_list.clear()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host_master, port=22, username='root', password='314315')
        ssh_list.append(ssh)
        global_dict["open_shell"] = True
        logger.info('连接-%s-成功' % os_name)
    except Exception as ret:
        logger.error(ret)


def send_cmd_windows(script_type, path, filename):
    """方法注释：
        Windows下发送shell命令
        'python3 /usr/python/spark_python_test.py'
        'ls -l;ifconfig' 多个命令用;隔开
    :param script_type:
    :param path: 脚本路径
    :param filename: 脚本文件名
    """
    try:
        if not global_dict["open_shell"]:
            start_ssh()
        cmd = None
        spark_cmd = get_cmd()
        if script_type == ScriptType.SCRIPT_PYTHON.value:
            cmd = 'ssh root@%s "%s /python3 %s/%s"' % (host_master, spark_cmd, path, filename)
        elif script_type == ScriptType.SCRIPT_JAVA.value:
            cmd = "暂不支持Java"
        stdin, stdout, stderr = ssh_list[0].exec_command(cmd)
        logger.info(cmd)
        return Default.OK.value
        # 接收输出或错误信息
        # result = stdout.read()
        # if not result:
        #     result = stderr.read()
        # print(result.decode())
    except Exception as e:
        global_dict["open_shell"] = False
        logger.error(e)
        return Default.NO.value


def send_cmd_linux(script_type, path, filename):
    """ 方法注释：
        Linux 下免密发送 shell 命令
        ssh root@192.168.8.9 "ls -l"
        'ls -l;ifconfig' 多个命令用;隔开
    :param script_type:
    :param path: 脚本路径
    :param filename: 脚本文件名
    """
    try:
        cmd = ''
        spark_cmd = get_cmd()
        if script_type == ScriptType.SCRIPT_PYTHON.value:
            cmd = 'ssh root@%s "%s /python3 %s/%s"' % (host_master, spark_cmd, path, filename)
        elif script_type == ScriptType.SCRIPT_JAVA.value:
            cmd = "暂不支持Java"
        os.system(cmd)
        logger.info(cmd)
        return Default.OK.value
    except Exception as e:
        logger.error(e)
        return Default.NO.value


def send_cmd(script_type, path, filename):
    """ 方法注释：
        发送 shell 命令，分 Windows 和 Linux
    :param script_type:
    :param path: 脚本路径
    :param filename: 脚本文件名
    """
    res = Default.NO.value
    if os_type == Default.OS_WINDOWS.value:
        res = send_cmd_windows(script_type, path, filename)
    elif os_type == Default.OS_LINUX.value:
        res = send_cmd_linux(script_type, path, filename)
    return res


def close():
    """方法注释：
        关闭 ssh 连接
    """
    for ssh in ssh_list:
        ssh.close()
    ssh_list.clear()


def get_source():
    """方法注释：
        内存使用情况，磁盘使用情况，CPU 使用情况
    """
    res = {}
    cmd_cpu = 'ssh root@192.168.43.61 sar -u 1 1'
    cmd_mem = 'ssh root@192.168.43.61 free -t'
    cmd_disc = 'ssh root@192.168.43.61 df'
    server_memory = get_mem_use(cmd_mem)
    server_disk_usage = get_disks_use(cmd_disc)
    cpu_use = get_cpu_use(cmd_cpu)

    server_dict = {'server_cpu': cpu_use, 'server_memory': server_memory, 'server_disk_usage': server_disk_usage}
    return server_dict


def get_cpu_use(cmd_cpu):
    """:方法注释：
        获取 CPU 使用率
    :param cmd_cpu:
    :return:
    """
    if os_type == Default.OS_WINDOWS.value:
        if not global_dict["open_shell"]:
            start_ssh()
        stdin, stdout, stderr = ssh_list[0].exec_command(cmd_cpu)
        # 接收输出或错误信息
        result = stdout.read()
        split_res = result.decode().split("\n")[-2]
        cpu_idle = ' '.join(split_res.split()).split(" ")[-1]
        # 接收输出或错误信息
        if not result:
            result = stderr.read()
    elif os_type == Default.OS_LINUX.value:
        res = os.popen(cmd_cpu).readlines()
        cpu_idle = ' '.join(res[-1].split()).split(" ")[-1]
    return 100 - float(cpu_idle.replace("'", ''))


def get_mem_use(cmd_mem):
    """:方法注释：
        获取 内存 使用率
    :param cmd_mem:
    :return:
    """
    if os_type == Default.OS_WINDOWS.value:
        if not global_dict["open_shell"]:
            start_ssh()
        stdin, stdout, stderr = ssh_list[0].exec_command(cmd_mem)
        # 接收输出或错误信息
        result = stdout.read()
        split_res = result.decode().split("\n")[-2]
        mem_use = ' '.join(split_res.split()).split(" ")[2]
        mem_total = ' '.join(split_res.split()).split(" ")[1]
        mem_idle = format(int(mem_use)/int(mem_total), '.2f')
        # 接收输出或错误信息
        if not result:
            result = stderr.read()
    elif os_type == Default.OS_LINUX.value:
        res = os.popen(cmd_mem).readlines()
        mem_use = ' '.join(res[-1].split()).split(" ")[2]
        mem_total = ' '.join(res[-1].split()).split(" ")[1]
        mem_idle = format(int(mem_use) / int(mem_total), '.2f')
    return mem_idle


def get_disks_use(cmd_disc):
    """:方法注释：
        获取 磁盘 使用率
    :param cmd_disc:
    :return:
    """
    if os_type == Default.OS_WINDOWS.value:
        if not global_dict["open_shell"]:
            start_ssh()
        stdin, stdout, stderr = ssh_list[0].exec_command(cmd_disc)
        # 接收输出或错误信息
        result = stdout.read()
        disk_idle = result.decode().split("\n")
        # 接收输出或错误信息
        if not result:
            result = stderr.read()
    elif os_type == Default.OS_LINUX.value:
        res = os.popen(cmd_disc).readlines()
        disk_idle = ' '.join(res[-1].split()).split(" ")
    return disk_idle


if __name__ == '__main__':
    print(get_source())
