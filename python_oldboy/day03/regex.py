#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : regex.py
@time   : 2016/7/19 21:50
@info   : 正则表达式
"""
import os, sys


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
    import re
    result1 = re.match('\d+','njk23k23') #重头开始匹配，支取一个，如果开头没有就不匹配后面
    if result1:
        print result1.group() # 匹配成功返回对象，匹配失败返回None
    else:
        print "noting"
    result2 = re.search('(\d+)\w*(\d+)','232jkj23j2k32') #匹配全部,只取一个
    if result2:
        print result2.group()
        print result2.groups() #('232', '2')
    result3 = re.findall('\d+','232j32k3j2k3j2k3j2')
    print result3   #['232', '32', '3', '2', '3', '2', '3', '2']

    pattern = re.compile('\d+')
    print pattern.findall('32434j3kjkj343')
    print pattern.match('32434j3kjkj343').group()
    print pattern.search('32434j3kjkj343').group()

    import time
    print time.time() #1468980577.39
    print time.struct_time  #
    print time.mktime(time.localtime()) #1468980631.0
    print time.gmtime() #time.struct_time(tm_year=2016, tm_mon=7, tm_mday=20, tm_hour=2, tm_min=12, tm_sec=39, tm_wday=2, tm_yday=202, tm_isdst=0)
    print time.strftime('%Y%m%d',time.localtime()) #20160720











