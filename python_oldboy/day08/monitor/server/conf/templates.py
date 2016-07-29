#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : templates.py
@time   : 2016/7/27 21:17
@info   : ??
"""
import os, sys

from service import  linux
class BaseTemplate(object):
    def __init__(self):
        self.name = 'yourTemplateName'
        self.group_name = 'YourGroupName'
        self.hosts = []
        self.services = []

class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(BaseTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.services = [linux.cpu,linux.memory]