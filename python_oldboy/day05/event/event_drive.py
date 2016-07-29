#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : event_drive.py
@time   : 2016/7/22 13:16
@info   : ??
"""
import os, sys

event_list = []

class BaseHandler(object):
    def execute(self):
        raise Exception('you must overwrite execute')


def run():
    for event in event_list:
        obj = event()
        obj.execute()

class MyHandler(BaseHandler):
    def execute(self):
        print 'event-drive execute MyHandler'

event_list.append(MyHandler)
run()
