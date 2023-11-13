# def binary_search(nums : list, target : int) -> int:
#     i, j = 0, len(nums) - 1
#     while i <= j:
#         mid = (i + j)//2
#         if nums[mid] < target:
#             i = mid + 1
#         elif nums[mid] > target:
#             j = mid - 1
#         else:
#             return mid
#     return mid
# a = [1,2,2,3,5]
# # print(binary_search(a, 1))
# # print(binary_search(a, 2))
# # print(binary_search(a, 3))

# # print(binary_search(a, 5))

# s = "32"
# print(s.isnumeric())
