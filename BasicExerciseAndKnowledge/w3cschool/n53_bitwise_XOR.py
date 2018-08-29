#coding:utf-8
# 题目：学习使用按位异或 ^ 。

for i in range(10):
    for j in range(10):
        if i ^ j:
            print '%d ^ %d = %d' % (i, j, i^j)

