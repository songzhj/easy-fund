#!/usr/bin/env python
#coding=utf-8

import config # 配置文件
import json
import crawler

def beauty_print(data):
    if data[1] > 0:
        print('%s\t| +%.2f%%' % data)
    else:
        print('%s\t| %.2f%%' % data)

valuation_url = config.URL['VALUATION']
for fund in config.FUND_LIST:
    percent = json.loads(crawler.get(valuation_url % (fund[0])))['data']['items'][-1]['percentage']
    beauty_print((fund[1], percent))
