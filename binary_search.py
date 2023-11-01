def binary_search(array, target):
    start, stop = 0, len(array) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            stop = mid - 1
        else:
            return mid
    
a = [1, 2, 3, 4]
print(binary_search(a, 2))