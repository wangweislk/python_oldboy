#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : index.py
@time   : 2016/7/20 14:16
@info   : ??
"""
import os, sys



if __name__ == '__main__':
    pass
    module = 'demo'
    method = 'Foo'
    demo = __import__(module)
    Foo = getattr(demo,method)
    Foo() # demo.Foo
    #这样做什么？ url 字符串解析对应的 control类处理
    #根据URL不同返回不同的值


