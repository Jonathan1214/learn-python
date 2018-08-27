#coding:utf-8
# 题目：打印出如下图案（菱形）diamond:
#    *           
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def print_diamond(num):
    '''
    para:必须是正奇数
    '''
    for i in range(num/2):
        print ' ' * (num/2 - i) + '*' * (2*i+1)

    print '*' * num

    for i in range(num/2):
        print ' ' * (i+1) + '*' * (2 * (num/2 - i) - 1)

print print_diamond(7)
