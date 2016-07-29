#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : global_settings.py
@time   : 2016/7/27 22:49
@info   : ??
"""
import os, sys
base_dir = os.path.dirname(os.path.dirname(__file__))
print base_dir
sys.path.append(base_dir)