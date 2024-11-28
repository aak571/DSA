# [4, 3, -2, 1] pivot = 1 [-2] + [1] + f([4, 3]) -> [3, 4] -> [-2, 1, 3, 4]

# [4, 3] pivot = 3 [] + [3] + [4] = [3, 4] -> return

# return [4, 3, -2, -1, 0] p = 4  [-2, -1, 0, 3] + [4] + f([]) =  [-2, -1, 0, 3, 4]     # l + p + r
# return [3, -2, -1, 0]  p = 3  [-2, -1, 0] + [3] + f([]) = [-2, -1, 0, 3]
# return [-2, -1, 0]  p = -2 f([]) + [-2] + [-1, 0] = [-2, -1, 0]
# return [-1, 0] p = -1   f([]) + [-1] + [0] = [-1, 0]
# return -> [0]


"""Qick Sort is a Divide and Conquer algorithm"""

# Time Complexity
# O(n*log(n)) -> best/avg case
# O(n^2) -> worst case

# Space Complexity
# O(log(n)) -> best/avg case
# O(n) -> worst case
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    l = []
    r = []

    for x in arr:
        if x < pivot:
            l.append(x)
        elif x > pivot:
            r.append(x)

    return quick_sort(l) + [pivot] + quick_sort(r)

nums = [10, 7, 8, 9, 1, 5]
sorted_list = quick_sort(nums)
print(sorted_list)

# print([0] + [1] + [2, 3])