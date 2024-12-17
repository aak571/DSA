# arr = [-1, 5, 1, 5, 1, 6]

# min = -1
# max = 6
# range = k = max - min + 1 = 6 - (-1) + 1 =   8  =  [-1, 0, 1, 2, 3, 4, 5, 6]

# count = [1, 0, 2, 0, 0, 0, 2, 1]
# loop {
# count[num - min] += 1
# num = -1    -1 - (-1) = 0
# num = 5      5 - (-1) = 6
# num = 1      1 - (-1) = 2
# num = 5      5 - (-1) = 6
# num = 1      1 - (-1) = 2
# num = 6      6 - (-1) = 7
# }

# cumulative count
# count = [0, 1, 1, 3, 3, 3, 3, 5]
# #        0  1  2  3  4  5  6  7
# output = [-1, 1, 1, 5, 5, 6] -> Sorted
# arr = [-1, 5, 1, 5, 1, 6]
# loop {
#     output[count[arr[i] - min] - 1] = arr[i]
#     count[arr[i] - min] -= 1

#     arr[i] = 6 o[c[6-(-1)]-1] = o[c[7]-1] = o[6-1] = o[5] = 6    c[7] - d
#     arr[i] = 1 o[c[1-(-1)]-1] = o[c[2]-1] = o[3-1] = o[2] = 1    c[2] - d
#     arr[i] = 5 o[c[5-(-1)]-1] = o[c[6]-1] = o[5-1] = o[4] = 5    c[6] - d
#     arr[i] = 1 o[c[1-(-1)]-1] = o[c[2]-1] = o[2-1] = o[1] = 1    c[2] - d
#     arr[i] = 5 o[c[5-(-1)]-1] = o[c[6]-1] = o[4-1] = o[3] = 5    c[6] - d
#     arr[i] = -1 o[c[-1-(-1)]-1] = o[c[0]-1] = o[1-1] = o[0] = -1 c[0] - d
# }

# n*3 = 3n = O(n)
#Time C -> O(n + k) -> best, avg, worst
#Space C -> O(k) -> best, avg, worst
def counting_sort(arr): #n          most of the times k will be greater than n
    # Step 1: Find the range of the input array
    if not arr:
        return []  # Handle edge case of empty array

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    # Step 2: Initialize the counting array
    count = [0] * range_of_elements # [0 ,0 ,0 ,0 ,0, 0] k

    # Step 3: Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Step 4: Compute cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):  # Traverse the input array in reverse
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

nums = [-1, 5, 1, 5, 1, 6]
print(counting_sort(nums))