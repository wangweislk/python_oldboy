#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : sqlhelper.py
@time   : 2016/7/21 17:33
@info   : ??
"""
import os, sys
import MySQLdb

#mysql操作
class MysqlHelper():
    def __init__(self):
        self.__mysql_dict = dict(host='localhost',user='root',passwd='root',db='dbname')
        pass

    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(**self.__mysql_dict)
        #数据连接
        pass

    def Get_One(self,sql,params):
        pass




