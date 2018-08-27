#coding:utf-8
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
#                假如兔子都不死，问每个月的兔子总数为多少?

# 一看到这个应该就可以用list储存或者写个生成器
def rabbits():
    '''
    斐波那契数列啊！
    '''
    m1 = 2 # 第一个月的兔子数
    m2 = 2 # 第二个月的兔子数
    while True:
        yield m1
        m1, m2 = m2, m1+m2

def how_in_months(month):
    i = 1   
    for rabbit in rabbits():
        if i == month:
            return rabbit
        i+=1

print how_in_months(10)