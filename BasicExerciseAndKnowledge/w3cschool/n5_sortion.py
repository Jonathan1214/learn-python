#coding:utf-8
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 有了sort函数感觉就是再开挂啊！！
import re

put_in = ['12 234 21']

lt = []
for num in put_in:
    nums = re.split(r'[\D]', num)
    for n in nums:
        lt.append(int(n))

lt = sorted(lt)
print lt