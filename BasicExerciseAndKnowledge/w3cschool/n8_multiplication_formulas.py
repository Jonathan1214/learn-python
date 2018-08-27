#coding:utf-8
# 题目：输出9*9乘法口诀表。

for i in range(1,10):
    for j in range(1,i+1):
        if j == i:
            print '%d * %d = %d\t' % (j, i, i*j)
        else:
            print '%d * %d = %d\t' % (j, i, i*j),

# for i, j  in zip(range(1,10), range(1,i+1)) if j == i print '%d * %d = %d\t' % (j, i, i*j) else print '%d * %d = %d\t' % (j, i, i*j),
# [(lambda i, j: print "{}*{}={}{}" % (i, j, i * j, "\n" if i == j else "\t"), end="")(j, i) for i in range(1, 10) for j in range(1, i + 1)]

print"\t".join([str(a) +"*"+ str(b) +"="+ str(a * b) for a in range(1, 10) for b in range(1, a+1) if a==b])