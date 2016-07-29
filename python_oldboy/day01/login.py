# -*- coding:utf-8 -*-

# Author : wangwei
# Date : 20160717 15:13
# Info : 模拟登陆:输入用户名和密码，登陆成功信息，连续输错三次锁定用户

import os
import sys

count = 3
acount_file = "acount.txt"      #存储用户名和密码
acount_lock = "acount_lock.txt" #存储被锁定的用户

while count > 0:
    username = raw_input("Please input username:")
    password = raw_input("Please input password:")

    lock_check = file(acount_lock)
    for line in lock_check.readlines():
        if username in line:
            sys.exit("%s is locked" % username)

    acount = file(acount_file,'rb')
    match_flag = False #默认为False，如果用户match上了，设置为True
    for line in acount.readlines():
        print line.split(' ')
        user,passwd = line.split(" ")

        if username == user and password == passwd:
            print 'Match:',True
            match_flag = True
            break
    acount.close()
    if not match_flag:
        count -= 1
        print "username or password error,please repeat input!"
    else:
        print "Wellcome %s !" % username
        break
else:
    print "Your acount %s is locked!" % username
    f = file(acount_lock,'ab')
    f.write(username)
    f.close()










