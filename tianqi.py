#!/usr/bin/python
#coding:gbk
#20140113

import urllib

url="http://www.weather.com.cn/beijing/index.shtml"
tel="13555555555"

tmp=[]
page=urllib.urlopen(url)
for i in page.readlines()[443:448]:
    a=i.strip()
    b=a.lstrip('<td>')
    test=b.rstrip('</td>')
    tmp.append(test)
page.close()
tianqi=','.join(tmp)


def SMS(x,y):
    smsurl="http://www.sms.com/warn?function=1000\&ms=%s&mo=%s" %(x,y)
    ms=urllib.urlopen(smsurl)
    ms.close()

SMS(tianqi,tel)
