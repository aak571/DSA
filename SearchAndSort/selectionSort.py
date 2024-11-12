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

# Selection Sort is better than Bubble Sort because it has lesser number of Swaps the Swapping expression
# is outside of the inner loop
def sort(nums):
    i = 0
    while i < len(nums) - 1:
        mi = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[mi]:
                mi = j
            j += 1
        nums[i], nums[mi] = nums[mi], nums[i]
        i += 1
    return nums

nums = [64, 25, 12, 22, 11]
print(sort(nums))



# [4, 3, 2, 1]

# i = 0  i < 3 mi = 0  j = 0+1=1
#    j = 1 j<4  mi = 3 SWAP

# [1, 3, 2, 4]

# i = 1  i < 3  mi = 1  j = 1+1=2
#   j = 2 j<4  mi = 2  SWAP

# [1, 2, 3, 4]

# i = 2  i < 3  mi = 2  j = 2+1=3
#   j = 3  j<4 mi=2 NO SWAP

# i = 3 i < 3
# [1, 2, 3, 4] -> final

# O(1) -> Space - constant
# O(n^2) -> Time