#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : threadingtest.py
@time   : 2016/7/25 11:58
@info   : ??
"""
import os, sys
import time
from threading import  Thread

def Foo(arg,arg2):
    for i in range(30):
        print i
        time.sleep(1)

print 'before'
t1 = Thread(target=Foo,args=(1,2,))
t1.setDaemon(True)
t1.start()
t1.join(5)  #主线程到达join，直到子线程结束才继续主线程。默认不超时，如果超过5s，超时后主线程不等待
print t1.getName()
#t1.setName('testthread')
print t1.isDaemon()  #False 等待子线程完成才结束主线程。True 主线程结束就退出，不等待子线程.是否守护
print t1.isAlive()

print 'after'
print 'after'
print 'after'
print 'after end'
time.sleep(10)





