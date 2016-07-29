# -*- coding:utf-8 -*-

# Author : wangwei
# Date : 20160717 15:13
# Info : 列表操作

import os,sys

def findId(lists,name):
    pos = 0
    for i in range(lists.count(name)):
        if pos == 0:
            pos = lists.index(name)
        else:
            pos = lists.index(name,pos+1)
        print 'Find Position:',pos



# sed 实现 ： 文件字符串替换
def sed(old_text,new_text,filename):
    f = file(filename,'rb')
    new_file = file('.%s.bak' % filename,'wb')
    for line in f.xreadlines():
        print line.replace(old_text,new_text)
        new_file.write(line.replace(old_text,new_text))
    f.close()
    new_file.close()

if len(sys.argv) < 4:
    print "Usage:python list_forloop.py old_text new_text filename"
    sys.exit()

old_text,new_text = sys.argv[1],sys.argv[2]
filename = sys.argv[3]
if '--bak' in sys.argv:
    bak_file = '%.bak' % filename
    os.system('mv %s %s.bak' % filename,filename)
else:
    bak_file = None







# lists = [1,2,3,4,5,3,2,4,5,65,2,2,3]
# findId(lists,2)

