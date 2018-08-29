#coding:utf-8
# 题目：学习使用按位与 & 。

# 先把十进制数转化为二进制数 再进行按位操作
for i in range(10):
    for j in range(10):
        if i & j:
            print '%d & %d = %d' % (i, j, i&j)


def convert_to_2base(num):
    '''
    把一个正整数转化为二进制数
    以字符串返回
    '''
    def helper(num):
        while num / 2:
            yield (num % 2)
            num /= 2
        yield 1

    lt = list(helper(num))[::-1]
    str_ = ''.join([str(item) for item in lt])
    return str_

print int(convert_to_2base(10), 2)
    


