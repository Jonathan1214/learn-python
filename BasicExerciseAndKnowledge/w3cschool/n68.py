#coding:utf-8
# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

list_ = list(x for x in range(1,20,2))
print list_
m = 2

for i in range(m):
    tmp = list_[-1]
    for count in range(len(list_)-1, 0, -1):
        list_[count] = list_[count-1]
    list_[0] = tmp
print list_
for i in range(len(list_)):
    print i
    list_.remove(list_[i])