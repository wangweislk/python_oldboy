#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : client.py
@time   : 2016/7/22 12:23
@info   : ??
"""
import os, sys
import socket

ip_port = ('127.0.0.1',8002)
sk = socket.socket()
sk.connect(ip_port)

while True:
    inp = raw_input('please input:')
    sk.sendall(inp)
sk.close()