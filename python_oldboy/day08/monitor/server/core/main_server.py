#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : main_serer.py
@time   : 2016/7/28 10:09
@info   : ??
"""
import os, sys
import global_settings
from redishelper import RedisHelper
import  serialize
import action_process

class MonitorServer(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.hosts = serialize.host_config_serialize()
        self.redis = RedisHelper()

    def handle(self):
        redis_sub = self.redis.subscribe()
        while True:
            msg = redis_sub.parse_response()
            print 'recv:',msg
            action_process.action_process(self,msg)
            print '---waiting for new msg ---'
            for host,val in self.hosts['hosts'].items():
                print host,val


    def run(self):
        self.handle()

    def process(self):
        pass

if __name__ == '__main__':
    pass