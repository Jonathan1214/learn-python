#coding:utf-8
# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# 第27个练习中的函数
def output(string,length):
    '''
    para: string 一行字符串
          length 字符串长度
    return 倒序输出字符串
    example input: 'Jonathan' len('Jonathan')
            output: n a h t a n o J
    '''
    if not length:
       return
    print(string[length-1]),
    output(string, length-1)  # 要返回值还是不要 注意把握！

num = 12345
num2str = str(num)
print len(num2str)
output(num2str, len(num2str))