#coding:utf-8
# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

lt = [32, 31, 43, 23]
print lt
def swap_max_and_first(list_):
    max_ = list_[0]
    index = 0
    for i in range(len(list_)):
        if max_ < list_[i]:
            max_ = list_[i]
            index = i
    list_[0], list_[index] = list_[index], list_[0]

def swap_min_and_last(list_):
    min_ = list_[0]
    index = 0
    for i in range(len(list_)):
        if min_ > list_[i]:
            min_ = list_[i]
            index = i
    list_[-1], list_[index] = list_[index], list_[-1]

swap_min_and_last(lt)
print lt
swap_max_and_first(lt)
print lt
