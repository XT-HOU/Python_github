# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""模块注释：
    python实现ssh功能
"""
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.8.9', port=22, username='root', password='314315')
cmd = 'python /usr/python/spark_python_test.py'
#cmd = 'ls -l;ifconfig'       #多个命令用;隔开
stdin, stdout, stderr = ssh.exec_command(cmd)

result = stdout.read()

if not result:
    result = stderr.read()
ssh.close()

print(result.decode())

if __name__ == '__main__':
    pass