#coding:utf-8
# 题目：对10个数进行排序

lt = [234, 2, 13, 4, 323, 45, 342, 34, 23, 654]

#Bubble sorting
def bubble_sorting(lt):
    for count in range(len(lt)):
        for i in range(len(lt)-count-1):
            if lt[i] > lt[i+1]:
                lt[i], lt[i+1] = lt[i+1], lt[i]
    return lt

print bubble_sorting(lt[:])

# Select sorting
def select_sorting(lt):
    '''
    选择排序：从未排序部分选出最小的放到已排序部分的最后面
    '''
    for i in range(len(lt)):
        min_ = lt[i]
        index = i
        for j in range(i,len(lt)):
            if lt[j] < min_:
                min_ = lt[j]
                index = j
        lt[index], lt[i] = lt[i], lt[index]

    return lt

print select_sorting(lt[:])


# Insert sorting
def insert_sorting(lt):
    for count in range(1,len(lt)):
        while lt[count] < lt[count-1] and count:
            lt[count], lt[count-1] = lt[count-1], lt[count]
            count -= 1
    return lt

print insert_sorting(lt)

# Merge sorting

