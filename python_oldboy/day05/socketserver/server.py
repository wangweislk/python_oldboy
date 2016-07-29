#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : server.py
@time   : 2016/7/22 10:42
@info   : ??
"""
import os, sys
#SocketServer - server
import SocketServer
class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        print self.request,self.client_address,self.server
        flag = True
        conn = self.request
        conn.send('hello')
        while flag:
            data = conn.recv(1024)
            print data
            if data == 'exit':
                flag = False
            conn.send('sb')


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('localhost',9999),MyServer)
    server.serve_forever()