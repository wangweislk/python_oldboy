#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : produce.py
@time   : 2016/7/25 14:17
@info   : 模拟生产者和消费者
"""
import os, sys
from threading import Thread
#先进先出队列，线程安全的
from Queue import Queue
import time

class Producer(Thread):

    def __init__(self,name,queue):
        Thread.__init__(self)
        '''
        :param name:生产者名称
        :param queue:队列
        :return:
        '''
        #私有变量
        self.__name = name
        self.__queue = queue

    def run(self):
        while True:
            if not self.__queue.full():
                self.__queue.put('baozi')
                print self.__name,'-生产了一个包子'
                time.sleep(0.5)
            else:
                print '容器满了'
                time.sleep(1)



class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self)
        self.__name = name
        self.__queue = queue

    def run(self):
        while True:
            if not self.__queue.empty:
                self.__queue.get()
                print self.__name,'-消费一个包子'
                time.sleep(1)
            else:
                print '容器没东西了'
                time.sleep(1)


q = Queue(maxsize=100)
# q.put('1')
# q.put('2')
# print q.qsize()
# print 'get:',q.get()
# print 'get:',q.get()

p1 = Producer('zhangsan',q)
p1.start()
p2 = Producer('lisi',q)
p2.start()


for item in range(20):
    name = 'wangwu%d' % item
    temp = Consumer(name,q)
    temp.start()