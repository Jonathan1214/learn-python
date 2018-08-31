#coding:utf-8
# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
#      问最后留下的是原来第几号的那位

#list.remove
# n = 37
# list_ = list(range(1,n+1))

# rem = 0
# for i in range(len(list_)):
#     if (i + 1 + rem) % 3 == 0:
#         list_.remove(list_[i])
# rem = len(list_) % 3
# while len(list_) > 1:
#     for i in range(len(list_)):
#         if (i + 1 + rem) % 3 == 0:
#             list_.remove(list_[i])
#     rem = len(list_) % 3
