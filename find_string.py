#!/usr/bin/python
#-*-coding:UTF-8 -*-#
#功能：查找文件中某个字符串出现的次数#
#用法：./find_string.py 文件名称 字符串名称#
#via: luwenju 2013-11-24

import re
import sys

filepath=sys.argv[1]
findstring=sys.argv[2]

f = open(filepath, "r+")
count=0
for i in f.readlines():
    li=re.findall(findstring, i)
    if len(li) > 0:
        count=count+1
print count
f.close()

