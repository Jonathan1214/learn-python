#coding:utf-8
# 题目：输出指定格式的日期
import time
import datetime
# 目的在于熟悉这个模块
print time.ctime()                     # localtime
print time.asctime(time.localtime())
print time.asctime(time.gmtime())      # gmt
print datetime.datetime(2018, 8, 12)
# print datetime.tzinfo
print datetime.date.today()
print datetime.date.fromtimestamp.__doc__