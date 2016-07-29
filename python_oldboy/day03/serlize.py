#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : serlize.py
@time   : 2016/7/19 21:17
@info   : 序列化和反序列化
"""
import os, sys


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

    import pickle
    data = ['wang','zhang',2,4,'wei']
    ser = pickle.dumps(data) #序列化
    print ser
    print type(ser) # <type 'str'>
    deser = pickle.loads(ser)
    print deser #['wang', 'zhang', 2, 4, 'wei']
    print type(deser) #<type 'list'>
    #序列化到文件
    pickle.dump(data,open('data.pk','w'))
    result = pickle.load(open('data.pk','r'))
    print result # ['wang', 'zhang', 2, 4, 'wei']

    #只能序列化常规的字典和列表
    import json
    data = {"name":"wangwei","age":24}
    json_ser = json.dumps(data)
    print json_ser #{"age": 24, "name": "wangwei"}
    print type(json_ser) #<type 'str'>
    json_deser = json.loads(json_ser)
    print json_deser #{u'age': 24, u'name': u'wangwei'}







