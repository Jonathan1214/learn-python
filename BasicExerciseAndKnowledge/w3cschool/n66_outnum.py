#coding:utf-8
# 题目：输入3个数a,b,c，按大小顺序输出。

a = 34
b = 42
c = 2
lt = []
lt.append(a)
lt.append(b)
lt.append(c)
lt.sort()
print lt[::-1]