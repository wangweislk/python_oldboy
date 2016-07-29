#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : ftp.py
@time   : 2016/7/22 15:34
@info   : ??
"""
import os, sys

import socket
ip_port = ('localhost',9999)
sk = socket.socket()
sk.connect(ip_port)
while True:
    input = raw_input('path:')
    cmd,path = input.split('|')

    filename = os.path.basename(path)
    filesize = os.stat(path).st_size()
    sk.send(cmd+'|'+filename+'|'+str(filesize))
    send_size = 0
    f = file(path,'rb')
    Flag = True
    while Flag:
        if send_size + 1024 > filesize:
            data  = f.read(filesize-send_size)
            Flag = False
        else:
            data = f.read(1024)
            send_size +=1024
        sk.send(data)
    f.close()
sk.close()

