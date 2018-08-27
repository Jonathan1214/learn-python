#coding:utf-8
# 题目：判断101-200之间有多少个素数，并输出所有素数

def is_prime(num):
    '''
    判断参数num是否是素数
    '''
    for i in range(2, num/2+1):
        if num % i == 0:
            return False
    return True

prime_lt = []
for num in range(101, 201):
    if is_prime(num):
        prime_lt.append(num)

print prime_lt
