#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : thread_event.py
@time   : 2016/7/25 17:47
@info   : ??
"""
import os, sys
import threading
import time

def producer():
    print '等人来买包子'
    event.wait() #阻塞等待
    event.clear()

    print 'sb is coming for baozi ..'
    print 'making a baozi for sb'
    time.sleep(5)
    print '你的包子好了'
    event.set()


def consumer():
    print '去买包子'
    event.set()

    time.sleep(2)
    print 'waiting for baozi to be ready'
    while True:
        # event.wait()
        if event.is_set():
            print '好吃'
            break
        else:
            print '尼玛还没好呀'
            time.sleep(1)




event = threading.Event()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()


