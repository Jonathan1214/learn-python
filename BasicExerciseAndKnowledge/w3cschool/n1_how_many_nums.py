#coding:utf-8
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

# 直接输出答案
print '直接输出答案'
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                print i, j, k


# 用list储存起来
print '\nlist储存起来在输出'
lt = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                tmp = i*100 + j*10 + k
                lt.append(tmp)

for n in lt:
    print n




# 试试生成器
print '\n试试生成器'
def get_nums():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i!=j) and (i!=k) and (j!=k):
                    # tmp = i*100 + j*10 + k
                    yield i*100 + j*10 + k

print get_nums() # get_nums返回一个生成器
for n in get_nums():
    print n
