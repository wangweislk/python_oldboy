#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : server.py
@time   : 2016/7/28 12:17
@info   : ??
"""
import os, sys
import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send(u"<h>hello word</h>")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8080))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()
        handle_request(conn)
        conn.close()
if __name__ == '__main__':
    main()