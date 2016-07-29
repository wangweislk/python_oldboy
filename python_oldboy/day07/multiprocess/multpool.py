#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : pool.py
@time   : 2016/7/25 23:30
@info   : ??
"""
import os, sys
from multiprocessing import Pool
import time

def f(x):
    print x
    time.sleep(1)
    return x*x


pool = Pool(processes=5)
res_list = []
for i in range(10):
    res = pool.apply_async(f,[i])
    res.get()
    # res_list.append(res)

# for res in res_list:
#     res.get()