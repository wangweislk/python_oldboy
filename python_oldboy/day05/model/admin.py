#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : admin.py
@time   : 2016/7/21 17:44
@info   : ??
"""
import os, sys
from utility.sqlhelper import MysqlHelper

class Admin(object):
    def __init__(self):
        # self.__helper = MysqlHelper()
        pass

    def get_name(self,id):
        sql = 'select * from admin where id = %s'
        params = (id,)
        result = MysqlHelper.Get_Dict()
        return result

    def checkValidata(self,username,password):
        sql = 'select * from admin username=%s and password=%s '
        params = (username,password,)
        # 查询数据库校验
        result = MysqlHelper.Get_One(sql,params)
        return result





