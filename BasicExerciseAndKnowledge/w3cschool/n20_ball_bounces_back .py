#coding:utf-8
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
h = 100 #反弹后的高度
sum_h = 100
for n in range(10):
    h /= 2.0
    sum_h += h * 2
    
print sum_h, h

