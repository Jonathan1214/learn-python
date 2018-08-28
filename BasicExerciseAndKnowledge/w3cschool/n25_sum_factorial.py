#coding:utf-8
# 题目：求1+2!+3!+...+20!的和。
def factorial(num):
    if num in (0, 1):
        return 1
    return factorial(num - 1) * num

print sum([factorial(num) for num in range(1, 21)])

def sum_factorial(num):
    '''
    计算前num项阶乘和
    '''
    for i in range(num,1,-1):  # 这里就用num表示结果 不再增加参数了
        num = (num + 1) * (i - 1)
    return num

print sum_factorial(20)