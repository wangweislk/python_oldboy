#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : multprocesstest.py
@time   : 2016/7/25 21:16
@info   : ??
"""
import os, sys
from multiprocessing import Pool
import time
from multiprocessing import Process,Queue,Value,Array,Manager

def Foo(x):
    time.sleep(1)
    print x
    return x*x

def info(title):
    print title
    print 'module name',__name__
    if hasattr(os,'getppid'):
        print 'parent id:',os.getpid()
    print 'process id:',os.getpid()

def f(name):
    info('function f')
    print 'hello',name

def fun(queue,id):
    queue.put([id,'hello'])

def fun2(n,a):
    n.value = 3.14
    for i in range(5):
        a[i] = -a[i]

def fun3(d,l):
    d[1] = 'l'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    pass
    #进程实例
    # p = Pool(5)
    # print p.map(Foo,range(100))

    #子进程和父进程关系
    # info('main line')
    # print '---------------'
    # p = Process(target=f,args=('bbb',))
    # p.start()
    # p.join()

    #进程通信--方式一，借助第三方桥梁
    # q = Queue()
    # for i in range(5):
    #     p = Process(target=fun,args=(q,i))
    #     p.start()
    # while True:
    #     print q.get()

    #方式二
    # num = Value('d',0.0)
    # arr = Array('i',range(10))
    # p = Process(target=fun2,args=(num,arr))
    # p.start()
    # p.join()
    # print num.value
    # print arr[:]

    #方式三
    m = Manager()
    d = m.dict()
    l = m.list(range(10))
    p = Process(target=fun3,args=(d,l))
    p.start()
    p.join()
    print d
    print l





