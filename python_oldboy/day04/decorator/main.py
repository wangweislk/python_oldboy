#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : main.py
@time   : 2016/7/20 15:39
@info   : ??
"""
import os, sys


#装饰器就是一个函数，用于装饰某个函数
def outer(fun):
    def wrapper():
        print 'cans'
        fun()
        print '验证之后'
    return wrapper

def outer2(fun):
    def wrapper(arg):
        print '参数'
        fun(arg)
        print '参数'
    return wrapper

def outer3(fun):
    def wrapper():
        print '参数'
        result = fun()
        print '参数'
        return result
    return wrapper

# Func1 = wrapper
@outer
def Func1():
    # print '验证'
    print 'Func1'

#有参数的函数
@outer2
def Func2(arg):
    print 'Func2',arg

#有返回值
@outer3
def Func3():
    return 'Func3'



if __name__ == '__main__':
    Func1()
    Func2('wangwwei')
    print Func3()

