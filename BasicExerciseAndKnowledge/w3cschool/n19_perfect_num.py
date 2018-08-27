#coding:utf-8
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def find_factor(num):
    '''
    找因子 忽略本身
    return: 因子组成的列表
    '''
    lt = []
    for i in range(1, num/2+1):
        if num % i == 0:
            lt.append(i)
    return lt

def is_PerfectNum(num):
    if sum(find_factor(num)) == num:
        return True
    return False

for num in range(1, 1001):
    if is_PerfectNum(num):
        print find_factor(num), num