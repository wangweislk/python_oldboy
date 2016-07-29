#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : thread_lock.py
@time   : 2016/7/25 17:03
@info   : ??
"""
import os, sys

import threading
import time

num = 0

def run(n):
    time.sleep(1)
    global  num
    lock.acquire()
    num += 1
    lock.release()
    print '%d\n' % num


lock = threading.Lock()
# lock = threading.RLock() # 递归锁
#信号量
samp = threading.BoundedSemaphore(4)



for i in range(100):
    t = threading.Thread(target=run,args=[i])
    t.start()