#coding:utf-8
# 题目：打印出杨辉三角形（要求打印出10行如下图）。

# lt_1 = [1]
# lt_2 = [1,1] # 起始条件

def print_pascal_triangle(num):
    lt_1 = [1]
    lt_2 = [1,1] # 起始条件
    print ' ' * (num - 1) + ' '.join([str(item) for item in lt_1])
    print ' ' * (num - 2) + ' '.join([str(item) for item in lt_2])
    for count in range(num-2):
        lt_1 = lt_2[:]
        for i in range(len(lt_1)-1):
            lt_2[i+1] = lt_1[i] + lt_1[i+1]
        lt_2.append(1)
        print ' ' * (num - count - 3) + ' '.join([str(item) for item in lt_2])

print_pascal_triangle(10)


#另一种写法
# if __name__ == '__main__':
#     a = []
#     for i in range(10):
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     for i in range(10):
#         a[i][0] = 1
#         a[i][i] = 1
#     for i in range(2,10):
#         for j in range(1,i):
#             a[i][j] = a[i - 1][j-1] + a[i - 1][j]
#     from sys import stdout
#     for i in range(10):
#         for j in range(i + 1):
#             stdout.write(str(a[i][j]))
#             stdout.write(' ')
#         print


