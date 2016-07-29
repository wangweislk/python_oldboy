#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : Person.py
@time   : 2016/7/21 12:50
@info   :
"""
import os, sys
import time

class Person(object):

    def __init__(self,name,sex,job='学生',stage='高中',salary=0,firend=None,relationship=[]):
        self.name = name
        self.sex = sex
        self.job  = job
        self.stage= stage
        self.salary = salary
        self.friend = firend
        self.relationship = relationship

    def toString(self):
        print self.name +'\t'+self.sex + '\t' +self.job +'\t' + self.stage +'\t' + str(self.salary) \
              +'\t' + str(self.friend.name if self.friend else 'nothing')





if __name__ == '__main__':
    jone = Person('Jone','男')
    liz = Person('Liz','女')
    peter = Person('Peter','男')
    jone.friend = liz
    liz.friend = jone
    jone.toString()
    liz.toString()
    peter.toString()


    for word in 'hello word!':

        sys.stdout.write(word)
        time.sleep(0.2)



