nums = [64, 34, 25, 12, 22, 22, 11, 90, 5] # asc
sorted = []
while len(nums) > 0:
    i = 0
    ind = -1
    g = float('-inf')
    while i < len(nums):
        if nums[i] >= g:
            g = nums[i]
            ind = i
        i += 1
    sorted.insert(0, g)
    nums.pop(ind)
print(sorted)

# O(n^2)