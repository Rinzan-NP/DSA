def recursioneg(list1 : list, index = 0,sum1 = 0 ):
    if index < len(list1):
        sum1 += list1[index]
        index += 1
        recursioneg(list1, index, sum1)
    return sum1
    


def add(list = []):
    num = int(input("enter no to be added :"))
    list.append(num)
    choice = input("Do you want to add another (y/n) :")
    if choice == "n":
        return list
    else:
        return add(list)


def factorial(nums, fact = 1):
    fact = nums * fact
    nums -= 1  
    if nums == 0:
        return  fact
    else:
        return factorial(nums, fact)
print(factorial(4))

