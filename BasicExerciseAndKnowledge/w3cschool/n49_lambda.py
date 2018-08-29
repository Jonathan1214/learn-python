#coding:utf-8
# 题目：使用lambda来创建匿名函数

# lambda 匿名函数 最多支持两个变量

MAXNUM = lambda x, y: (x > y) * x + (x < y) * y

MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

print MAXNUM(10, 20)
print MINIMUM(10, 20)

