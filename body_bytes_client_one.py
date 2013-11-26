#!/usr/bin/env python
#-*-coding:UTF-8 -*-#
#功能：单个域名流量查询 #
#via: luwenju 2013-11-26

import datetime

t1=datetime.datetime.now()
t2=t1+datetime.timedelta(minutes=-1)
pasttime=t2.strftime('%d/%b/%Y:%H:%M:')

log_path="/opt/log/access.log"
list=[]
findfile=open(log_path)
for i in findfile.readlines():
    line=i.strip()
    if pasttime in line:
        nem=line.split(" ")[9]
        nem=int(nem)
        list.append(nem)
#print "%s byte" %sum(list) #byte
print "%s Mbps" %(float(sum(list)) / 1024 / 1024 * 8) #Mb
findfile.close()
