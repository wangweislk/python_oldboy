#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : consumer_producer.py
@time   : 2016/7/25 16:35
@info   : ??
"""
import os, sys
import threading
import time
import Queue
import random

def producer(name,queue):
    while True:
        queue.put('baozi')
        print 'Made a baozi ......................',name
        time.sleep(random.randrange(3))

def consumer(name,queue):
    while True:
        try:
            data = queue.get_nowait()
            print 'Got a baozi ...',name
        except Exception,e:
            print '没有包子了...'
        time.sleep(random.randrange(5))

q = Queue.Queue()
p1 = threading.Thread(target=producer,args=['zhangsan',q])
p2 = threading.Thread(target=producer,args=['wangwu',q])
p1.start()
p2.start()


c1 = threading.Thread(target=consumer,args=['lisi',q])
c2 = threading.Thread(target=consumer,args=['zhaoliu',q])
c1.start()
c2.start()