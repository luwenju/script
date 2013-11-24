#!/usr/bin/python
#-*-coding:UTF-8 -*-#
#功能：Nginx访问日志切割#
#用法：./nginx_log_remove.py 日志文件路径#
#via: luwenju 2013-11-24

import os
import shutil
import time

time=time.strftime('%Y%m%d')

srcpath="/opt/log/www.58.com/www.58.com_access.log"
dstpath="/opt/log/www.58.com/www.58.com_access_%s.log" %(time)

if os.path.exists(srcpath):
    shutil.move(srcpath, dstpath)
    os.system('kill -USR1 `cat /var/run/nginx.pid`')
else:
    print "File does not exist!"
