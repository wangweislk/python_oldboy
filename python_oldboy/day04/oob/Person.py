#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : Person.py
@time   : 2016/7/20 16:27
@info   : ??
"""
import os, sys
import time

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


#动态字段属于对象
class Province(object):

    #静态字段属于类
    desc = '中国34个省市之一'

    # self 是实例化的对象(hb = Province('河北','石家庄','wangwi')) hb
    # 构造函数，初始化对象时执行
    def __init__(self,name,capital,leader,flag=False):
        self.name = name
        self.capital = capital
        self.leader = leader
        #私有字段，对象不能访问
        self.__tailand = flag

    #析构函数，对象执行完后执行
    def __del__(self):
        print '解释器销毁 ... '

    #调用 obj()对象时执行的方法
    def __call__(self, *args, **kwargs):
        print args   #()
        print kwargs #{}
        print  'call ...'

    def sports_meet(self):
        print self.name+',正在开运动会...'

    @staticmethod  #动态方法变成静态方法，去掉self参数
    def Foo():
        print '反腐倡廉...'

    @property #方法变成属性
    def Bar(self):
        print self.name

    #给是有字段提供对外访问方法
    def getTailand(self):
        print self.__tailand

    #私有变量，只读属性
    @property
    def Tailand(self):
        return self.__tailand

    #私有变量，只写属性.obj.Tailand = True
    @Tailand.setter
    def Tailand(self,value):
        self.__tailand = value

    #私有方法
    def __sha(self):
        print '私有方法 ...'

#
# hb = Province('河北','石家庄','wangwi')  #执行__init__()方法
# print hb.name       #河北
# print hb.desc       #中国34个省市之一，对象访问静态字段
# print Province.desc #中国34个省市之一，属于类
# hb.sports_meet()
# Province.Foo()
# hb.Bar      #河北
# #调用私有方法，不建议使用
# hb._Province__sha()
# print hb.Tailand  # False
# hb.Tailand = True
# print hb.Tailand  # True
# hb()  #执行__call__()方法  #call ...


#如果继承object叫做新式类，如果没有继承object叫经典类
class Father(object):

    desc = 'falter desc ...'
    def __init__(self):
        self.name = 'fathername'
        print 'Father 初始化  ... '

    def Func(self):
        print 'Father.Func ... '

    def Bad(self):
        print 'Father.Bad 抽烟 喝酒 ... '

#继承Father
#Son叫子类，也叫派生类
class Son(Father):
    def __init__(self):
        self.name = 'sonname'
        print 'Son 初始化...'
        #调用父类构造函数
        Father.__init__(self)  # Father 初始化  ...
        super(Son,self).__init__()  #父类必须继承object  #Father 初始化  ...

    def Bar(self):
        print 'Son.Bar .... '

    # def Bad(self):
    #     print '重写父类方法 ... '

    def Bad(self):
        #调用父类方法
        Father.Bad(self)   # Father.Bad 抽烟 喝酒 ...
        print 'Son.Bad .... '

son = Son()   #Son 初始化...
print son.desc   #falter desc ...
son.Func() #Father.Func ...
son.Bar()  #Son.Bar ....
son.Bad()  #重写父类方法 ...



#新式类和经典类的区别
class A(object):
    def __init__(self):
        print 'this is A ..'
    def save(self):
        print 'A.save '

class B(A):
    def __init__(self):
        print 'this is B'
class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'C.save'

class D(B,C):
    def __init__(self):
        print 'this is D'

d = D() #this is D

# d.save() #A.save   #先搜索第一个继承B---> A --->C  (深度优先)
d.save()   #C.save   #集类继承object(新式类)，搜索方法为 B ---> C  ---> A


#接口：抽象类+抽象方法
from abc import ABCMeta,abstractmethod
class Alter:
    __metaclass__ =  ABCMeta

    @abstractmethod
    def send(self):pass


class Foo(Alter):
    def __init__(self):
        print 'Foo.init ...'

    def send(self):
        print 'send weixin ...'

f = Foo()  #Foo.init ...
f.send()   #send weixin ...