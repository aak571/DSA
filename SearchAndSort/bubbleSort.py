# nums = [64, 34, 25, 12, 22, 22, 11, 90, 5] # asc
# sorted = []
# while len(nums) > 0:
#     i = 0
#     ind = -1
#     g = float('-inf')
#     while i < len(nums):
#         if nums[i] >= g:
#             g = nums[i]
#             ind = i
#         i += 1
#     sorted.insert(0, g)
#     nums.pop(ind)
# print(sorted)

# O(n^2)


# nums = [64, 34, 25, 12, 22, 22, 11, 90, 5]
# nums = [4, 3, 2, 1]

# 1
# 4, 3, 2, 1
# 3, 4, 2, 1
# 3, 2, 4, 1
# 3, 2, 1, 4

# 2
# 2, 3, 1, 4
# 2, 3, 1, 4
# 2, 1, 3, 4

# 3
# 1, 2, 3, 4

# i < len(nums) - 1

nums = [64, 34, 25, 12, 22, 22, 11, 90, 5]
nums = [4, 3, 2, 1] # [1, 2, 3, 4]
i = 0
while i < len(nums) - 1:
    j = 0
    while j < len(nums) - i - 1:
        if nums[j] > nums[j + 1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        j += 1
    i+=1
print(nums)

# 4 3 2 1
# 0 1 2 3

# i = 0
# j < 4-0-1 = 3
# 3 4 2 1
# j = 1
# 3 2 4 1
# j = 2
# 3 2 1 4
# j = 3  (F) STOP

# i = 1
# j < 4-1-1

nums = [48, 32, 21, 78, 5] # [1, 2, 3, 4]
i = 0
for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1): # (0, 4) = [0, 1, 2, 3]
        if nums[j] > nums[j + 1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        j += 1
    i+=1
print(nums)

# for i in range(30, 35):
    # print(i)

