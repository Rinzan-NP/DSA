def recursioneg(list1 : list, index = 0,sum1 = 0 ):
    if index < len(list1):
        sum1 += list1[index]
        index += 1
        return recursioneg(list1, index, sum1)
    return sum1
    


print(recursioneg([1,2,3,4]))