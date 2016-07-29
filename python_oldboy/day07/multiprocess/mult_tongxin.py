#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : mult_tongxin.py
@time   : 2016/7/25 22:32
@info   : ??
"""
import os, sys

from multiprocessing import Process,Queue

def f(queue,id):
    queue.put([id,'hello'])

if __name__ == '__main__':
    #进程通信--借助第三方桥梁
    q = Queue()
    for i in range(5):
        p = Process(target=f,args=(q,i))
        p.start()
    print q.get()