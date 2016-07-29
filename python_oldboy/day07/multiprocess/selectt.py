#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : selectt.py
@time   : 2016/7/26 20:24
@info   : ??
"""
import os, sys
import select
import socket
import Queue

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)

ip_port = ('localhost',9999)
print >>sys.stderr,'starting up on %d port % s' % ip_port
server.bind(ip_port)

server.listen(5)