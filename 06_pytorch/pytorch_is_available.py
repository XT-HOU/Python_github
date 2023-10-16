# ！/usr/bin/python3
# -*- coding:utf-8 -*-

"""文档注释：
验证 pytorch 是否安装成功
"""
__author__ = "HOU"

if __name__ == '__main__':
    import torch
    print(torch.__version__)
    print(torch.cuda.is_available())
