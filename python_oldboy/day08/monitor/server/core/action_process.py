#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : action_process.py
@time   : 2016/7/28 10:18
@info   : ??
"""
import os, sys
import pickle
import serialize

def action_process(server_instance,msg):
    msg = pickle.loads(msg[2])
    func_name = msg.keys()[0]
    func = getattr(serialize,func_name)
    func(server_instance,msg[func_name])