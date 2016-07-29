#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : select.py
@time   : 2016/7/22 12:16
@info   : ??
"""
import os, sys

#利用select监听终端操作
import select
import threading
import sys
while True:
    readable,writeable,error = select.select([sys.stdin,],[],[],1)
    for stdin in readable:
        print stdin.readline()