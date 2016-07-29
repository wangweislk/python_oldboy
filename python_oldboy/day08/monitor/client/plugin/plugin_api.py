#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : plugin_api.py
@time   : 2016/7/28 9:52
@info   : ??
"""
import os, sys
import cpu,memory

def get_cpu_info():
    return cpu.monitor()

def get_memory_info():
    return memory.monitor()