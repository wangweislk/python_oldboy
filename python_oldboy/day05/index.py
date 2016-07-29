#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : index.py
@time   : 2016/7/21 15:23
@info   : ??
"""
import os, sys
from model.admin import Admin

def main():
    user = raw_input('username:')
    pwd = raw_input('password:')
    admin = Admin()
    result = admin.checkValidata(user,pwd)
    print result

if __name__ == '__main__':
    main()

