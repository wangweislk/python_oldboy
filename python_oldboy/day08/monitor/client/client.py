#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : client.py
@time   : 2016/7/28 9:13
@info   : ??
"""
import os, sys
import threading
from redishelper import RedisHelper
import pickle
import time
from plugin import plugin_api

host_ip = '192.168.1.101'

class MonitorClient(object):
    def __init__(self,server,port):
        self.server = server
        self.port = port
        self.configs = {}
        self.redis = RedisHelper()

    def get_configs(self):
        value = self.redis.get('HostConfig::%s' % host_ip)
        if value:
            self.configs =pickle.load(value)
            return True
        return False

    def handle(self):
        if self.get_configs():
            print '--going to monitor services-- ',self.configs
            while True:
                for service_name,val in self.configs['services'].items():
                    interval,plugin_name,last_check = val
                    if time.time() - last_check >= interval:
                        t = threading.Thread(target=self.task,args=[service_name,plugin_name])
                        t.start()
                        self.configs['serivces'][service_name][2] = time.time()
                    else:
                        next_run_time = interval - (time.time()-last_check)
                        print '%s will be run in next %s seconds' % (service_name,next_run_time)
                time.sleep(1)

        else:
            print '--could not found any configuration for this host---'

    def task(self,service_name,plugin_name):
        print '---going to run service:',service_name
        func = getattr(plugin_api,plugin_name)
        result = func()
        self.redis.public(pickle.dump(result))

    def run(self):

        self.handle()


if __name__ == '__main__':
    client = MonitorClient('172.0.0.1',6379)
    client.run()