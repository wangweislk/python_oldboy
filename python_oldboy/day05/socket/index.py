#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : index.py
@time   : 2016/7/21 21:41
@info   : ??
"""
import os, sys

import socket

#http://localhost:8080/
def handler_request(conn):
    buf = conn.recv(1024)
    conn.send('HTTP/1.1 200 OK\r\n\r\n')
    conn.send('hello wei')

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    sock.bind(('localhost',8080))
    sock.listen(5)

    while True:
        conn , addr = sock.accept()
        handler_request(conn)
        conn.close()


if __name__ == '__main__':
    main()