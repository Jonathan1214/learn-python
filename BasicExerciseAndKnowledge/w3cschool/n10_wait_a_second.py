#coding:utf-8
# 题目：暂停一秒输出
# 这里就当作是了解time这个module了
import time

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# 2018-08-25 10:39:05
# 暂停一秒
time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

tl = time.localtime()
print type(tl)
# <type 'time.struct_time'>
print tl[7]
# 237
print time.asctime(tl)
# Sat Aug 25 10:39:39 2018