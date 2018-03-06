#!/usr/bin/env python
#coding=utf-8

import json

with open('all_fund_list') as f:
    print len(json.loads(f.read()))