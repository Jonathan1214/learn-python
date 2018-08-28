#coding:utf-8
# 题目：利用递归方法求5!。

def factorial(num):
    if num in (0,1):
        return 1
    return factorial(num-1) * num

print(factorial(5))