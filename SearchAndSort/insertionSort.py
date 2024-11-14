# [12, 11, 13, 5, 6] -> asc

# [12, 12, 13, 5, 6] key = 11
# [11, 12, 13, 5, 6]

# [11, 12, 13, 5, 6] key = 13

# [11, 12, 13, 5, 6] key = 5
# [11, 12, 13, 13, 6]
# [11, 12, 12, 13, 6]
# [11, 11, 12, 13, 6]
# [5, 11, 12, 13, 6]

# [5, 11, 12, 13, 6] key = 6
# [5, 11, 12, 13, 13]
# [5, 11, 12, 12, 13]
# [5, 11, 11, 12, 13]
# [5, 6, 11, 12, 13]

# Insertion Sort is prefered when ur list is small only (Because the no.of operations are more if the size of list is more)
# Swapping does not use a 3rd party variable behind the scenes instead it uses 'Tuple Unpacking'
def sort(nums):
    i = 1
    while i < len(nums):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        i += 1
    return nums

nums = [12, 11, 13, 5, 6]
print(sort(nums))

# O(n^2)
# O(1) - constant

def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
nums = [12, 11, 13, 5, 6]
print(sort(nums))

# i = 1   i < 5  key = 11  j = 0
#     j >= 0 and nums[0] > 11
#     num[1] = nums[0]
#     nums[1] = 11  [12, 11, 13, 5, 6]
#     j = -1  F

# i = 2  i < 5  key = 13  j = 1
#     nums[2] = nums[1]  F

# i = 3  i < 5  key = 5  j = 2
#     nums[3] = nums[2]  [11, 12, 13, 13, 6]
#     j = 1
#     nums[2] = nums[1]  [11, 12, 12, 13, 6]
#     j = 0
#     nums[1] = nums[0]  [11, 11, 12, 13, 6]
#     j = -1  F
# nums[0] = 5  [5, 11, 12, 13, 6]

# i = 4   i < 5 key = 6  j = 3
#     nums[4] = nums[3]  [5, 11, 12, 13, 13]
#     j = 2
#     nums[3] = nums[2]  [5, 11, 12, 12, 13]
#     j = 1
#     nums[2] = nums[1]  [5, 11, 11, 12, 13]
#     j = 0
#     F
# nums[1] = 6  [5, 6, 11, 12, 13]