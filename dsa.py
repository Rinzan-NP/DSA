def string_last(strings ):
    splitted = strings.split()
    return splitted[-1]

# print(string_last("This is my country"))

def merge_sort_desc(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        right = nums[mid:]
        left = nums[:mid]
        merge_sort_desc(right)
        merge_sort_desc(left)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k +=1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k +=1
        return nums


def pivot_place(nums, start, end):
    pivot = nums[start]
    i = start + 1
    j = end
    while True:
        while i >= j and nums[i] >= pivot :
            i += 1
        while i <= j and nums[j] <= pivot:
            j -= 1
        if i > j:
            break
        nums[i],nums[j] = nums[j],nums[i]
    nums[j], nums[start] = nums[start], nums[j]
    return j

def quick_sort(nums, start, end):
    if start < end:
        pi = pivot_place(nums, start, end)
        quick_sort(nums, start, pi - 1)
        quick_sort(nums, pi +  1, end)
    return nums

a = [5, 4, 2, 3, 1]
quick_sorted = quick_sort(a, 0, len(a)- 1)
print(quick_sorted)