#coding:utf-8
# 题目：将一个列表的数据复制到另一个列表中。
# 切片就OK

lt1 = [1,3,5,5]
lt2 = lt1[:]  # 保留副本
lt1[2] = 343
print lt2
print lt1
