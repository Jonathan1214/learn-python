#coding:utf-8
# 题目：企业发放的奖金根据利润提成。
#      利润(I)低于或等于10万元时，奖金可提10%；
#      利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#      20万到40万之间时，高于20万元的部分，可提成5%；
#      40万到60万之间时高于40万元的部分，可提成3%；
#      60万到100万之间时，高于60万元的部分，可提成1.5%，
#      高于100万元时，超过100万元的部分按1%提成，
#      从键盘输入当月利润I，求应发放奖金总数？

# 一个简单的分段函数问题

# 非常难看的if嵌套
def get_bonus(profit):
    bonus = 0
    if profit < 0:
        print '无效输入！！'
        return None
    if profit <= 100000:
        bonus = profit * 0.1
    elif profit <= 200000:
        bonus = 10000 + (profit - 100000) * 0.075
    elif profit <= 400000:
        bonus = 10000 + 7500 + (profit - 200000) * 0.05
    elif profit <= 600000:
        bonus = 10000 + 7500 + 10000 + (profit - 400000) * 0.03
    elif profit <= 1000000:
        bonus = 10000 + 7500 + 10000 + 6000 + (profit - 600000) * 0.015
    else:
        bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (profit - 1000000) * 0.01

    return bonus

if __name__ == '__main__':
    profits = [1324243, 54353233, 34354361, 4354354, 31234, 465462]
    bonuses = []
    for profit in profits:
        if get_bonus(profit): # 这里其实有问题的 当是profit是0的时候 bonus也是0 但会被判错
            bonuses.append(get_bonus(profit))

    for bonus in bonuses:
        print bonus




