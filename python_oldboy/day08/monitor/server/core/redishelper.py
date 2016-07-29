#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : redishelper.py
@time   : 2016/7/27 20:26
@info   : ??
"""
import os, sys
import redis

class RedisHelper():
    def __init__(self):
        self.__conn = redis.Redis(host='localhost')
        self.chan_sub = 'channel1'
        self.chan_pub = 'channel1'
    def get(self,key):
        return  self.__conn.get(key)
    def set(self,key,value):
        self.__conn.set(key,value)
    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

if __name__ == '__main__':
    rh = RedisHelper()
    rh.public('test')