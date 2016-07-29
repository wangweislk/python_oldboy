#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : index.py
@time   : 2016/7/20 14:25
@info   : ??
"""
import os, sys
import logging


if __name__ == '__main__':
    pass
    #输入格式： acount/login
    url = raw_input('请输入地址：')
    arr = url.split('/')
    print arr
    if len(arr)==2:
        try:
            namespace = __import__('backend.'+arr[0])
            module = getattr(namespace,arr[0])
            method = getattr(module,arr[1])
            method()
        except (ImportError,AttributeError),e:
            print '导入模块错误',e
            logging.info(e)
            logging.warn(e)
        except Exception,e:
            print e
        else:
            print '没有出错'
        finally:
            print '无论如何都执行'

    else:
        print 'url 错误 404 ... '


