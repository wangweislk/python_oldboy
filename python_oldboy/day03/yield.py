#!/usr/bin/env python
# coding:utf-8
"""
@version: ??
@author : wangwei
@file   : yield.py
@time   : 2016/7/19 10:53
@info   : yield 操作
"""

#生成一个生成器，只有遍历的时候才会创建值
def func():
    yield 1
    yield 2
    yield 3

def xreadlines():
    seek = 0
    while True:
        with open('file/demo','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return


if __name__ == '__main__':
    pass
    # yd = func()
    # print yd
    # for item in yd:
    #     print item
    # print xreadlines()
    #
    # for line in xreadlines():
    #     print line.strip()

    #三元运算符
    result = 'gt' if 1 > 3 else 'lt'

    #lambda表达式
    a = lambda  x,y : x+y
    # print a(1,2)  # 3

    #内置函数
    a = [1,2,3]
    print help(a)
    print dir(a)
    print vars()
    print type(a) #<type 'list'>
    import os
    reload(os)
    abs(-1)
    cmp(1,2)
    bool(1)
    divmod(2,4)
    max([1,2])
    min([1,2])
    sum([1,2])
    pow(1,1)
    len('')
    all([]) #只要一个元素为False，结果为False
    any([]) #只要一个元素为True，结果为True

    chr(66) # B ascii码装字符
    ord('B') # 66 字符装ascii码
    hex(2) #十六进制
    bin(2) #二进制
    oct(2) #八进制

    range(10)
    xrange(10)
    li = ['a','b','c','d']
    for id,value in enumerate(li,1): #增加序列ID号
        print id,value

    s = 'i am {0} {1}'
    print s.format('weiw','hi')

    def func1(arg):
        print arg
    # apply(func1,('aaaa'))

    def func2(v):
        return v+100
    print map(func2,[1,2,3]) # [101, 102, 103]

    print filter(lambda x:x>1,[1,2,3]) # [2, 3]

    print reduce(lambda x,y:x+y ,[1,2,3]) # 6

    x = [1,2,3]
    y = [2,3,4]
    z = [3,4,5]
    print zip(x,y,z) # [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

    a = '8 * 8'
    print eval(a)

    #反射
    temp = 'sys' #字符串话的模块名称
    sys = __import__(temp) #通过这种方式导入os模块
    print sys.path #['C:\\Users\\bbd\\PycharmProjects\\python_oldboy\\day03',....]

    # import mysql
    # import sqlserver
    # print sqlserver.count()
    # print mysql.count()

    #采用模块字符串话反射导入模块
    model = __import__("mysql")
    print model.count() # 1
    model = __import__("sqlserver")
    print model.count() # 2

    #以字符串的形式执行函数
    #delattr
    #hasattr
    mysql_module = __import__("mysql")
    count_func = getattr(mysql_module,"count")
    print count_func() # 1

















