#coding:utf-8
# 题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

# 最简单的枚举法 
import math
def is_full_square(num):
    '''
    判断一个小于100000的数是否是完全平方数
    '''
    for i in range(350):
        if i**2 == num:
            return True

def find_num():
    fns = [] # 就用list吧 其实可以换成生成器
    for i in range(100000):
        if is_full_square(i+100) and is_full_square(i+268):
            fns.append(i)
    return fns

for i in find_num():
    print i
# print 21 261 1518
# [Finished in 1.7s]
# 可以断定就这些了 因为在往上的话 两个完全平方数之间的差距肯定大于168 那么肯定找不到这样的数了

# 其实好傻呀我

# 好好想想吧！！有库不用！！
# 给的答案 运行时间0.1s
for i in range(10000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print i
# [Finished in 0.1s]