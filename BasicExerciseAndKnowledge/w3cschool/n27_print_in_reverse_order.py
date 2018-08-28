#coding:utf-8
# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

string = 'Jonathan'

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
output(string, len(string))
