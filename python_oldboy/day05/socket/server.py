#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : server.py
@time   : 2016/7/21 22:02
@info   : ??
"""
import os, sys

# socket - server
import socket
sk = socket.socket()
ip_port = ('localhost',9999)
sk.bind(ip_port)
sk.listen(5)
while True:
    conn,add = sk.accept()
    conn.send('hello')
    flag = True
    while flag:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()