#coding:utf-8
# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

lt = [8,7,6,4,3,1]

num2insert = 5

def insertnum(num, lt):
    lt.append(num)
    count = len(lt) - 1
    if lt[-2] > lt[0]:
        while lt[count] < lt[count-1] and count:
            lt[count], lt[count-1] = lt[count-1], lt[count]
            count -= 1
    else:
        while lt[count] > lt[count-1] and count:
            lt[count], lt[count-1] = lt[count-1], lt[count]
            count -= 1

    return lt
print insertnum(num2insert, lt[:])


