#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : random_checkcode.py
@time   : 2016/7/19 15:49
@info   : random验证码生成
"""
import os, sys



if __name__ == '__main__':
    import random
    print random.random()
    print random.randint(1,5) # >=1 and <=5
    print random.randrange(1,10) # >=1 and <10

    print ord('A'),ord('Z')
    zm = chr(random.randint(65,90))
    code = []
    for i in range(6):
        if i == random.randint(1,5):
            code.append(str(random.randint(0,9)))
        else:
            code.append(chr(random.randint(65,90)))
    print ''.join(code)
