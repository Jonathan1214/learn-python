#coding:utf-8
# 题目：斐波那契数列。
# 想想有多少种方法去写这个东西

# 方法一
def fibs(num):
    n1 = 0
    n2 = 1
    i = 1
    while i < num:
        n1, n2 = n2, n1+n2
        i += 1
    return n1

lt = []
for i in range(1,10):
    lt.append(fibs(i))
for n in lt:
    print n
