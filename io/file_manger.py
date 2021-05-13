# ！/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import datetime

filePath = '/io/deal/'
print(datetime.datetime.now())


def readfile():
    return os.listdir(filePath)


for name in readfile():
    path = os.path.join(filePath, name)
    if not os.path.isdir(path):
        with open(filePath + name) as f:
            for line in f.readlines():
                with open(filePath + 'deal/' + name, 'a') as m:
                    m.writelines(' '.join(line.split()))
                    m.write('\n')

print(datetime.datetime.now())
