#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : hosts.py
@time   : 2016/7/27 21:17
@info   : ??
"""
import os, sys
import templates

g1 = templates.LinuxTemplate()
g1.group_name = 'Test groups'
g1.hosts = ['192.168.1.101','192.168.1.103']

monitored_groups = [g1]