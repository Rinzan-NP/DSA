def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1
    

def selection_sort(list1):
    for i in range(len(list1)):
        minimum = i
        for j in range(i , len(list1)):
            if list1[minimum] > list1[j]:
                minimum = j
        list1[i],list1[minimum] = list1[minimum], list1[i]
    return list1
    

def merge_sort(nums):
    if len(nums) <= 1:
        return  nums
    mid = len(nums) // 2
    left =  nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i , j , k = 0, 0 , 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k]=left[i]
            i += 1
        else:
            nums[k]=right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] =  left[i]
        k += 1
        i += 1
    while j < len(right):
        nums[k] =  right[j]
        k += 1
        j += 1
    return nums


def insertion_sort(nums):
    for i in range(1,len(nums)):
        j = i
        while j > 0  and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


def pivot_place(nums, first, last):
    pivot = nums[first]
    left = first + 1
    right = last
    while True:
        while left <= right and nums[left] <= pivot:
            left += 1
        while left <= right and nums[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            nums[right], nums[left] = nums[left], nums[right]
    nums[right], nums[first] = nums[first], nums[right]
    return right

def quick_sort(nums, first, last):
    if first < last:
        right = pivot_place(nums, first, last)
        quick_sort(nums, first, right - 1)
        quick_sort(nums, right +  1, len(nums) - 1)
    return nums



# bubble = bubble_sort(a)
# selection = selection_sort(a)
# merge = merge_sort(a)
# insert = insertion_sort(a)
# quick = quick_sort(a, 0, len(a) - 1)
# print(f"bubble sort : {bubble}")
# print(f"Selection sort : {selection}")
# print(f"Merge sort : {merge}")
# print(f"Insertion sort : {insert}")
# print(f"Quick sort : {quick}")

def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] > arr[l]:
        smallest = l

    if r < n and arr[smallest] > arr[r]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

a = ["Ant", "Bat", "Cat", "Dog"]
print(f"After heap sort (desc) : {heapSort(a)}")