#coding:utf-8
# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
from fractions import Fraction, gcd

Denomi_1 = 1
Denomi_2 = 2

numer_1 = 2
numer_2 = 3
sum_ = Fraction(numer_1, Denomi_1) + \
       Fraction(numer_2, Denomi_2)
for count in range(19):
    numer_1, numer_2 = numer_2, numer_1 + numer_2
    Denomi_1, Denomi_2 = Denomi_2, Denomi_1 + Denomi_2
    sum_ += Fraction(numer_1, Denomi_1) + Fraction(numer_2, Denomi_2)

print float(sum_)
print int(sum_)

