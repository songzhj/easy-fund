#!/usr/bin/env python
#coding=utf-8
import time
import json
import crawler
import config
import random

all_fund = None
with open('all_fund_list') as f:
    all_fund = json.loads(f.read())

# 每10s请求一次，写入文件
with open('all_fund_detail2', 'w+') as f:
    for i in all_fund:
        f.write(crawler.get(config.URL['DETAIL'] % (i)) + '\n')
        time.sleep(random.randint(1, 5))