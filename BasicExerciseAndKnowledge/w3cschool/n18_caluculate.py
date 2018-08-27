#coding:utf-8
# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制
n = 4
a = 2
t = 0
lt = []
for count in range(n):
    t = t + a
    a = a * 10
    lt.append(t)
    print t

lt = reduce(lambda x,y: x+y, lt)
print 'result: '+str(lt)