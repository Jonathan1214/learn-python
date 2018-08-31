#coding:utf-8
# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
#      每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
import re
def encryption(passwords):
    '''
    传入4位字符密码
    '''
    pw = re.findall(r'[\d]', passwords)
    pw2list = [int(item) for item in pw]

    for i in range(4):
        pw2list[i] = (pw2list[i] + 5) % 10

    pw2list[0], pw2list[3] = pw2list[3], pw2list[0]
    pw2list[1], pw2list[2] = pw2list[2], pw2list[1]

    _passwords = ''.join([str(item) for item in pw2list])
    return _passwords

print encryption('3451')


