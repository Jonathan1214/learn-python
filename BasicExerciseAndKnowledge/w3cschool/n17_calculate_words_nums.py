#coding:utf-8
# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

# 1.英文字母
# 2.空格
# 3.数字
# 4.其他字符
# 正则表达式！！！！牛逼正则！
import re
string = 'fdsff 23sdsf 1e`!dds32 dsr fdfg'

def calculate_nums(string):
    '''
    string是一行字符串
    返回英文字母、空格、数字和其他字符个数
    '''   
    letter_nums = len(re.findall(r'[a-zA-Z]', string))
    space_nums = len(re.findall(r'\s', string))
    digital_nums = len(re.findall(r'\d', string))
    others = len(re.findall(r'\W', string))
    return letter_nums, space_nums, digital_nums, others

print calculate_nums(string)

