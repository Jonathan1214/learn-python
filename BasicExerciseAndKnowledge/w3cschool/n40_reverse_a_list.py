#coding:utf-8
# 题目：将一个数组逆序输出。

lt = [12, 34, 45, 43]

def print_in_reverse(lt):
    for item in lt[::-1]:
        print item,

print_in_reverse(lt)
