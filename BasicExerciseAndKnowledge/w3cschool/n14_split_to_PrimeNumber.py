#coding:utf-8
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 我做的好像差一点 不过影响不大

def is_prime(num):
    '''
    判断参数num是否是素数
    '''
    for i in range(2, num/2+1):
        if num % i == 0:
            return False
    return True

def find_factor(num):
    '''
    找因子 忽略1和本身
    '''
    lt = []
    for i in range(2, num/2+1):
        if num % i == 0:
            lt.append(i)
    return lt

def split_to_PrimeList(num):
    '''
    如果num是合数 返回质因数分解元素 如90拆成2 3 3 5 储存在list中返回
    若是素数 返回空
    '''
    try:                                   # 如果num是素数 lt则为空 引发IndexError
        lt = find_factor(num)              # 临时储存num的因子
        # if not lt:
        #     return lt
        factor_lt = []                     # 储存质因子
        factor_lt.append(lt[0])            # 显然 lt的第一个元素必然是质数
        factor_lt.append(lt[-1])           # 第一个和最后一个的乘积就是这个数

        while not is_prime(factor_lt[-1]): # 当质因数list中最后一个大数不是素数
            lt = find_factor(factor_lt[-1])
            factor_lt[-1] = lt[0]
            factor_lt.append(lt[-1])

        return factor_lt
    except IndexError:
        return None

def print_PrimeFactors(lt, num):
    if lt:
        print '\n'
        i = 1
        for item in lt:
            if i != len(lt):
                print '%d *' % item,
            else:
                print '%d = %d' % (item, num),
            i += 1
    else:
        print '\n%d不是素数' % num

if __name__ == '__main__':
    # num = int(raw_input('请输入一个合数：'))
    # print_Prime(split_to_PrimeList(num), num)
    for num in range(1,1000):
        print_PrimeFactors(split_to_PrimeList(num), num)



    
        