#!/usr/bin/env python
#coding=utf-8

import re
import json
import crawler

data = crawler.get('http://money.finance.sina.com.cn/fund/view/vNewFund_FundListings.php').decode('gbk')
reg = r'title=["\'].*?\((\d*?)\)["\']'
handle_data = re.findall(reg, data)
with open('all_fund_list', 'w') as f:
    f.write(json.dumps([i for i in handle_data if i], ensure_ascii = False))