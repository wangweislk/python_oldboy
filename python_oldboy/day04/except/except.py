#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : except.py
@time   : 2016/7/21 12:07
@info   : 自定义类
"""
import os, sys

class MyException(Exception):
    def __init__(self,msg):
        self.error = msg

    def __str__(self,*args,**kwargs):
        return self.error

exp = MyException('错了')
print exp   #错了
#手动触发异常
try:
    1+1
    raise  MyException('自定义错误')
except Exception,e:
    print e    #自定义错误