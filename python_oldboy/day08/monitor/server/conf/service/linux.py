#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : linux.py
@time   : 2016/7/27 20:53
@info   : ??
"""
import os, sys
import generic
from data_process import avg,hit,last

class cpu(generic.BaseService):
    def __init__(self):
        super(cpu,self).__init__()
        self.name = 'linux_cpu'
        self.interval = 30
        self.plugin_name = 'get_cpu_status'
        self.trigger = {
            'idle':{
                'func':avg,
                'minutes':15,
                'operator':'lt',
                'threshhold':0,
                'warning':20,
                'critical':5,
                'data_type':'percentage'
            },
            'iowait':{
                'func':hit,
                'minutes':10,
                'operator':'gt',
                'threshhold':3,
                'warning':50,
                'critical':80,
                'data_type':'int'
            }
        }

class memory(generic.BaseService):
    def __init__(self):
        super(memory,self).__init__()
        self.name = 'linux_memory'
        self.interval = 60
        self.plugin_name = 'get_memory_status'
        self.trigger = {
            'usage':{
                'func':avg,
                'minutes':15,
                'operator':'lt',
                'threshhold':0,
                'warning':80,
                'critical':90,
                'data_type':'percentage'
            }
        }
