# [64, 25, 12, 22, 11] - Sort in asc

# start from ind 0 and swap 11 with 64
# [11, 25, 12, 22, 64]

# start from ind 1 and swap 12 with 25
# [11, 12, 25, 22, 64]

# start from ind 2 and swap 22 with 25
# [11, 12, 22, 25, 64]

# start from ind 3 and swapping not required because 25 is already in the first place.
# [11, 12, 22, 25, 64] -> Sorted List

# O(n^2)


def sort(nums):
    i = 0
    while i < len(nums) - 1:
        mi = i
        j = i + 1
        while j < n:
            if nums[j] < nums[mi]:
                mi = j
            j += 1
        nums[i], nums[mi] = nums[mi], nums[i]
        i += 1
    return nums

nums = [64, 25, 12, 22, 11]
print(sort(nums))