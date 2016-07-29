#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : generic.py
@time   : 2016/7/27 20:50
@info   : ??
"""
import os, sys

class BaseService(object):
    def __init__(self):
        self.name = 'BaseService'
        self.interval = 300
        self.last_time = 0
        self.plugin_name = 'your plugin name'
        self.trigger = {}

