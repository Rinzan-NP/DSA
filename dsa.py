import heapq
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

# a = [5, 4, 2, 3, 1]
# quick_sorted = quick_sort(a, 0, len(a)- 1)
# print(quick_sorted)

def heapify(nums, index, end):
    l, r = 2 * index + 1, 2 * index + 2
    largest = index
    if l < end and nums[l] > nums[largest]:
        largest = l
    if r < end and nums[r] > nums[largest]:
        largest = r
    if largest != index:
        nums[largest], nums[index] = nums[index], nums[largest]
        heapify(nums, largest, end)


def heap_sort(nums):
    n = len(nums) 

    for i in range(n//2 - 1, -1, -1):
        heapify(nums, i, n )
    
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)
    return nums




# heap = []
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 2)
# print(heap)
# print(heapq.heappop(heap))
# print(heap)

def validate(tree):
    def is_validate(node, left, right):
        if node is None:
            return True
        if not left < node.val < right:
            return False
        return is_validate(node.left, left, node.val) and is_validate(node.right, node.val, right)
    return is_validate(tree, float('-inf'), float('inf'))

def pre_order(tree):
    elements = []
    elements.append(tree.val)
    if tree.left:
        elements += pre_order(tree.left)
    elif tree.right:
        elements +=  pre_order(tree.right)
    return elements


def heap_add(heap : list, val : int):
    heap.append(val)
    i = len(heap) - 1
    while i != 0 and heap[(i - 1 )// 2] < heap[i]:
        heap[i], heap[(i - 1 )// 2] = heap[(i - 1 )// 2], heap[i]
        i = (i - 1) // 2

def heapify(heap, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < len(heap) and heap[smallest] > heap[left]:
        smallest = left
    if right < len(heap) and heap[smallest] > heap[right]:
        smallest = right
    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        heapify(smallest)


        

        
