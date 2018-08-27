#coding:utf-8
# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
#       例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方

for num in range(101, 1000):
    hd_digit = num / 100
    ten_digit = (num - hd_digit * 100) / 10
    single_digit = num % 10
    if hd_digit**3 + ten_digit**3 + single_digit**3 == num:
        print num



