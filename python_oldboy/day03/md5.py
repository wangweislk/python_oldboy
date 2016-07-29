#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : md5.py
@time   : 2016/7/19 21:05
@info   : ??
"""
import os, sys


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
    import hashlib
    hash = hashlib.md5()
    hash.update('admin')
    print hash.hexdigest() # 21232f297a57a5a743894a0e4a801fc3

