#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : client.py
@time   : 2016/7/21 22:04
@info   : ??
"""
import os, sys

# socket - client
import socket
client = socket.socket()
ip_port = ('localhost',9999)
client.connect(ip_port)
while True:
    data = client.recv(1024)
    print data
    inp = raw_input('client:')
    client.send(inp)
    if inp == 'exit':
        print '退出'
        break