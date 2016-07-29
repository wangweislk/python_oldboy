#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : paramiko_ssh.py
@time   : 2016/7/25 15:12
@info   : ??
"""
import os, sys

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost',22,'root','root')
stdin,stdout,stderr = ssh.exec_command('df')
print stdout.read()
ssh.close()


private_key_path = '/home/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('localhost',22,username='root',pkey=key)
stdin,stdout,stderr = ssh.exec_command('df')
print stdout.read()
ssh.close()
