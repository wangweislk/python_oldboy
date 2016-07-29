#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : server.py
@time   : 2016/7/23 10:45
@info   : ??
"""
import os, sys

import SocketServer

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'C:/temp'
        conn = self.request
        print 'connected ... '
        while True:
            pre_data = conn.recv(1024)
            #获取请求方法、文件名、文件大小
            cmd,filename,filesize = pre_data.split('|')
            #已经接受文件大小
            recv_size = 0
            #上传文件路径拼接
            file_dir = os.path.join(base_path,filename)
            f = file(file_dir,'wb')
            Flag = True
            while Flag:
                #文上传文件
                if int(filesize) > recv_size:
                    #最多可以接受1024，可能小于1024
                    data = conn.recv(1024)
                    recv_size += len(data)
                #上传完毕，退出
                else:
                    recv_size = 0
                    Flag = False
                    continue
                #写文件
                f.write(data)
            print 'upload successed'
            f.close()
instance = SocketServer.ThreadingTCPServer(('localhost',9999),MyServer)
instance.serve_forever()