#coding:utf-8
# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 输入格式：2018 08 24
# 输出格式：***

# python2中的input函数可以获得数字输入 raw_input获得字符串输入
# python3中没有raw_input了，只有input，所有输入均被视为字符串
import re
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nonleap_year = leap_year[:]
nonleap_year[1] = 28

def is_leap_year(year):
    '''
    判断是否是闰年 是返回True 否则是平年返回False
    '''
    if (year % 4) == 0 or (year % 40) == 0 or (year % 400) == 0:
        return True
    return False

def get_year_month_day(date):
    '''
    模拟输入的字符串日期
    返回年、月、日
    '''
    dat = re.split(r'[\D]', date)
    return int(dat[0]), int(dat[1]), int(dat[2])



if __name__ == '__main__':
    # 模拟输入
    date_put_in = ['2018 08 23', '2000 01 16', '2001 01 08']
    for date in date_put_in:
        year, month, day = get_year_month_day(date)
        if is_leap_year(year):
            days = sum(leap_year[:month-1]) + day
        else:
            days = sum(nonleap_year[:month-1]) + day

        print days
# print sum(leap_year[:2-1])