#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : serialize.py
@time   : 2016/7/27 22:31
@info   : ??
"""
import os, sys
# from conf import hosts
import global_settings
from conf import hosts
import pickle
import time
from redishelper import RedisHelper

def host_config_serialize(host_ip):
    applied_services = []
    configs = {
        'services':{}
    }
    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
            applied_services.extend(group.services)
    applied_services = set(applied_services)
    for service in applied_services:
        service = service()
        configs['services'][service.name] = [service.interval,service.plugin_name,0]
    print configs
    return configs

def flush_all_host_configs_into_redis():
    applied_hosts = []
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    applied_hosts = set(applied_hosts)

    redishelper = RedisHelper()
    for host in applied_hosts:
        host_config = host_config_serialize(host)
        key = 'HostConfig::%s' % host
        redishelper.set(key,pickle.dump(host_config))
    return True

def report_service_data(server_instance,msg):
    host_ip = msg['ip']
    service_status_data = msg['data']
    service_name = msg['service_name']
    server_instance.hosts['hosts'][host_ip][service_name] = {
        'data':service_status_data,
        'timestamp':time.time()
    }
    key = 'StatusData::%s' % host_ip
    server_instance.redis.set(key,pickle.dump(service_status_data.hosts['hosts'][host_ip][service_name]))


if __name__ == '__main__':
    host_config_serialize('192.168.1.101')