#!/usr/bin/env python
#coding=utf-8
import time
import json

all_fund = None
with open('all_fund_list') as f:
    all_fund = json.loads(f.read())

# 每10s请求一次，写入文件
with open