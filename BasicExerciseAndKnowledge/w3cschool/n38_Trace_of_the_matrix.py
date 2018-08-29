#coding:utf-8
# 题目：求一个3*3矩阵对角线元素之和。
# 再多想一点 能不能写个求行列式值的函数？

matrix_33 = [[1,2,3],[4,5,6],[7,8,9]]

def trace(lt):
    '''
    para: lt 必须是方阵
    '''
    trace = 0
    for i in range(len(lt)):
        for j in range(len(lt)):
            if i == j:
                trace += lt[i][j]
    return trace

if __name__ == '__main__':
    print trace(matrix_33)


