#coding:utf-8
# 题目：暂停一秒输出。
# 这个题没有什么意义 我要去熟悉time这个module就好了
import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1) # 暂停 1 秒