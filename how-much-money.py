#!/usr/bin/env python
#coding=utf-8

year = input('输入年限：')
base_money = input('每月投资金额：')
year_profit = input('输入年利润:')
month_profit = year_profit / 12;
total_month = year * 12

result = base_money;
for i in range(total_month):
    result *= (1 + month_profit)
    result += base_money

print('%d 年后的结果：%s' % (year, format(result, ',.2f')))