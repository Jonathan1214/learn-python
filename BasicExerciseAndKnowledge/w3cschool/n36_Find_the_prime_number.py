#coding:utf-8
# 题目：求100之内的素数

def is_prime(num):
    '''
    判断参数num是否是素数
    '''
    for i in range(2, num/2+1):
        if num % i == 0:
            return False
    return True

for num in range(2,100):
    if is_prime(num):
        print num

