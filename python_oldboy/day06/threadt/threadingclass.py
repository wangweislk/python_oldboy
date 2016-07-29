#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : threadingclass.py
@time   : 2016/7/25 12:23
@info   : 自定义线程类
"""
import os, sys

from threading import  Thread
import time

class MyThread(Thread):
    def run(self):
        print 'iam thread'

def Bar(arg):
    print 'Bar'
t = MyThread(target=Bar,args=(1,))
t.start()