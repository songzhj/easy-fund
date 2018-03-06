#coding=utf-8

import urllib2

# 爬取url的数据
def get(url):
    # 模拟浏览器用户标识
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(url = url,headers = headers)
    return urllib2.urlopen(req).read()
