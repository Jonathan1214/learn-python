#coding:utf-8
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
def is_palindrome(num):
    '''
    para: num 的位数必须是奇数 
          若是偶数则引发ValueError
    return: num如果是回文数 True 否则 False
    '''
    num2str = str(num)
    num_of_digits = len(num2str)
    if num_of_digits % 2: # 位数为奇
        flag = 1          # 标志位 1表示num为回文数
        for count in range(num_of_digits/2):
            if num2str[count] != num2str[-(count+1)]:
                flag = 0
                break
        if flag:
            return True
        return False
    else:
        raise ValueError

print is_palindrome(12321)
print is_palindrome(3423)

