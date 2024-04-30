# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
    paramik封装
    TODO 未测试完可修改
"""
import paramiko

__author__ = "HOU"


class SFTPClient:
    """注释：
        paramiko SFTPClient 工具类
    """

    def __init__(self, host='XXX.XXX.XXX.XXX', port=22, username='XXX', pwd='XXX'):
        """注释：
            初始化连接创建Transport通道
        :param host:远程ip地址
        :param port:端口
        :param username:用户名
        :param pwd:密码
        """
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__transport = paramiko.Transport(self.host, self.port)
        self.__transport.connect(username=self.username, password=self.pwd)
        self.sftp = paramiko.SFTPClient.from_transport(self.__transport)

    def close(self):
        """注释：
            关闭通道
        :return:
        """
        self.sftp.close()
        self.__transport.close()

    def upload(self, local_path, remote_path):
        """注释：
            上传文件
        :param local_path: 本地路径
        :param remote_path: 远程路径
        :return:
        """
        self.sftp.put(localpath=local_path, remotepath=remote_path)

    def download(self, local_path, remote_path):
        """注释：
            下载文件
        :param local_path: 本地路径
        :param remote_path: 远程路径
        :return:
        """
        self.sftp.get(localpath=local_path, remotepath=remote_path)

    def mkdir(self, remote_path, mode='0777'):
        """注释：
            远程主机创建文件夹
        :param remote_path: 远程路径
        :param mode: 文件夹权限
        :return:
        """
        self.sftp.mkdir(path=remote_path, mode=mode)

    def rmdir(self, remote_path):
        """注释：
            远程主机创建文件夹
        :param remote_path: 远程路径
        :return:
        """
        self.sftp.rmdir(path=remote_path)

    def listdir(self, remote_path):
        """注释：
            查看路径下文件及文件夹
        :param remote_path: 远程路径
        :return:
        """
        list_file = self.sftp.listdir(path=remote_path)
        return list_file

    def remove(self, remote_path):
        """注释：
            删除文件
        :param remote_path:远程路径+filename
        :return:
        """
        self.sftp.remove(remote_path)

    def listdir_arr(self, remote_path):
        """注释：
            查看路径下文件及文件夹的详细信息
        :param remote_path: 远程路径
        :return:
        """
        try:
            list_file = self.sftp.listdir_attr(path=remote_path)
            return list_file
        except:
            raise Exception("获取信息失败！")

    def stat(self, file_path):
        """注释：
            获取文件详细信息
        :param file_path: 远程路径+filename
        :return:
        """
        return self.sftp.stat(file_path)


class SSHClient:
    """注释：
        paramiko SSHClient 工具类
    """
    def __init__(self, host='XXX.XXX.XXX.XXX', port=22, username='XXX', pwd='XXX'):
        """注释：
            初始化连接,需关闭连接
        :param host:远程ip地址
        :param port:端口
        :param username:用户名
        :param pwd:密码
        """
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.SSH = paramiko.SSHClient()
        self.SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.SSH.connect(hostname=host, port=port, username=username, password=pwd)

    def close(self):
        """注释：
            关闭连接
        :return:
        """
        self.SSH.close()

    def cmd(self, command):
        """注释：
            SSH 远程主机执行命令
        :param command:
        :return:
        """
        stdin, stdout, stderr = self.SSH.exec_command(command=command)
        result = stdout.read()
        if not result:
            result = stderr.read()
        return result
