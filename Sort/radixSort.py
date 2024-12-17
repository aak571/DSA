# # Time Complexity - O(k.n) - k is the maximum digits and n is the length of list
# # Space Complexity - O(n + b) - n is the length of list and b is range (0 to 9)

# """Radix Sort is not inherently designed to handle negative numbers and decimal values because it
#     processes numbers digit-by-digit, and negative numbers include a - sign and decimal point that cannot
#     be handled directly in the standard implementation. However, with modifications, Radix Sort can be
#     adapted to handle negative numbers effectively."""

# """Radix Sort works well for decimal numbers when:
# 1. Precision (number of decimal places) is known or can be standardized.
# 2. A stable and efficient sorting algorithm is required."""


# arr = [501, 408, 3, 24]
# max = max(arr) = 501 = max is 3 digits

# Sort it by it's units place - [501, 2, 24, 408] - Counting Sort

# #Set the count to zeros
# count = [0, 1, 0, 1, 1, 0, 0, 0, 1, 0] # 0 - 9 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #        0  1  2  3  4  5  6  7  8  9

# #Set the output to zeros
# output = [0, 0, 0, 0]
# #         0  1  2  3

# exp = 1
# loop {
#     arr[i] = 501    index = (arr[i] // exp) % 10 = (501 // 1) % 10 = 501 % 10 = 1
#     c[index] += 1

#     arr[i] = 408    index = (arr[i] // exp) % 10 = (408 // 1) % 10 = 408 % 10 = 8
#     c[index] += 1

#     arr[i] = 3      index = (arr[i] // exp) % 10 = (3 // 1) % 10 = 3 % 10 = 3
#     c[index] += 1

#     arr[i] = 24     index = (arr[i] // exp) % 10 = (24 // 1) % 10 = 24 % 10 = 4
#     c[index] += 1
# }

# #cumulative count
# loop {
#     count  = [0, 0, 1, 1, 2, 3, 3, 3, 3, 4]
#     #         0  1  2  3  4  5  6  7  8  9
# }

# output = [501, 3, 24, 408]
# #          0   1  2    3

# #construct the output
# i = len(arr) - 1
# loop {
#     arr[i] = 24
#     index = (arr[i] // exp) % 10 = (24 // 1) % 10 = 24 % 10 = 4
#     o[c[index] - 1] = arr[i] -> o[2] =  24
#     c[index] -= 1

#     arr[i] = 3
#     index = (arr[i] // exp) % 10 = (3 // 1) % 10 = 3 % 10 = 3
#     o[c[index] - 1] = arr[i] -> o[1] =  3
#     c[index] -= 1

#     arr[i] = 408
#     index = (arr[i] // exp) % 10 = (408 // 1) % 10 = 408 % 10 = 8
#     o[c[index] - 1] = arr[i] -> o[3] =  408
#     c[index] -= 1

#     arr[i] = 501
#     index = (arr[i] // exp) % 10 = (501 // 1) % 10 = 501 % 10 = 1
#     o[c[index] - 1] = arr[i] -> o[0] =  501
#     c[index] -= 1
# }






# arr = [501, 003, 024, 408]
# Sort it by it's ten's place - [501, 3, 408, 24] - Counting Sort

# #Reset the count back to zeros
# count = [3, 0, 1, 0, 0, 0, 0, 0, 0, 0] # 0 - 9 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #        0  1  2  3  4  5  6  7  8  9

# #Reset the output back to zeros
# output = [0, 0, 0, 0]
# #         0  1  2  3

# exp = 10
# loop {
#     arr[i] = 501    index = (arr[i] // exp) % 10 = (501 // 10) % 10 = 50 % 10 = 0
#     c[index] += 1

#     arr[i] = 3      index = (arr[i] // exp) % 10 = (3 // 10) % 10 = 0 % 10 = 0
#     c[index] += 1

#     arr[i] = 24     index = (arr[i] // exp) % 10 = (24 // 10) % 10 = 2 % 10 = 2
#     c[index] += 1

#     arr[i] = 408    index = (arr[i] // exp) % 10 = (24 // 10) % 10 = 40 % 10 = 0
#     c[index] += 1
# }

# #cumulative count
# loop {
#     count  = [0, 3, 3, 4, 4, 4, 4, 4, 4, 4]
#     #         0  1  2  3  4  5  6  7  8  9
# }

# output = [501, 003, 408, 024]
# #          0    1    2    3

# #construct the output
# i = len(arr) - 1
# loop {
#     arr[i] = 408
#     index = (arr[i] // exp) % 10 = (408 // 10) % 10 = 40 % 10 = 0
#     o[c[index] - 1] = arr[i] -> o[2] =  408
#     c[index] -= 1

#     arr[i] = 24
#     index = (arr[i] // exp) % 10 = (24 // 10) % 10 = 2 % 10 = 2
#     o[c[index] - 1] = arr[i] -> o[3] =  24
#     c[index] -= 1

#     arr[i] = 3
#     index = (arr[i] // exp) % 10 = (3 // 10) % 10 = 0 % 10 = 0
#     o[c[index] - 1] = arr[i] -> o[1] =  3
#     c[index] -= 1

#     arr[i] = 501
#     index = (arr[i] // exp) % 10 = (501 // 10) % 10 = 50 % 10 = 0
#     o[c[index] - 1] = arr[i] -> o[0] =  501
#     c[index] -= 1
# }






# arr = [501, 003, 408, 024]
# Sort it by it's hundred's place - [003, 024, 408, 501] - Counting Sort

# #Reset the count back to zeros
# count = [2, 0, 0, 0, 1, 1, 0, 0, 0, 0] # 0 - 9 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #        0  1  2  3  4  5  6  7  8  9

# #Reset the output back to zeros
# output = [0, 0, 0, 0]
# #         0  1  2  3

# exp = 100
# loop {
#     arr[i] = 501    index = (arr[i] // exp) % 10 = (501 // 100) % 10 = 5 % 10 = 5
#     c[index] += 1

#     arr[i] = 3      index = (arr[i] // exp) % 10 = (3 // 100) % 10 = 0 % 10 = 0
#     c[index] += 1

#     arr[i] = 408    index = (arr[i] // exp) % 10 = (408 // 100) % 10 = 4 % 10 = 4
#     c[index] += 1

#     arr[i] = 24     index = (arr[i] // exp) % 10 = (24 // 100) % 10 = 0 % 10 = 0
#     c[index] += 1
# }

# #cumulative count
# loop {
#     count  = [0, 2, 2, 2, 3, 3, 4, 4, 4, 4]
#     #         0  1  2  3  4  5  6  7  8  9
# }

# output = [3, 24, 408, 501] -> final sorted list
# #         0   1   2    3

# #construct the output
# i = len(arr) - 1
# loop {
#     arr[i] = 24
#     index = (arr[i] // exp) % 10 = (24 // 100) % 10 = 0 % 10 = 0
#     o[c[index] - 1] = arr[i] -> o[1] =  24
#     c[index] -= 1

#     arr[i] = 408
#     index = (arr[i] // exp) % 10 = (408 // 100) % 10 = 4 % 10 = 4
#     o[c[index] - 1] = arr[i] -> o[2] =  408
#     c[index] -= 1

#     arr[i] = 3
#     index = (arr[i] // exp) % 10 = (3 // 100) % 10 = 0 % 10 = 0
#     o[c[index] - 1] = arr[i] -> o[0] =  3
#     c[index] -= 1

#     arr[i] = 501
#     index = (arr[i] // exp) % 10 = (501 // 100) % 10 = 50 % 10 = 5
#     o[c[index] - 1] = arr[i] -> o[3] =  501
#     c[index] -= 1
# }


def counting_sort(arr, exp):
    """
    A helper function that performs counting sort on `arr` based on the digits place.
    """
    n = len(arr)
    output = [0] * n  # Output array to hold sorted elements -> [0, 0, 0, 0]
    count = [0] * 10  # Digits always range from 0 to 9 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Count occurrences of each digit in the given place (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # The below code is to build the cumulative list from left to right if you want to sort in ascending order
    i = 1
    while i < 10:
        count[i] += count[i - 1]
        i = i + 1

    # The below code is to build the cumulative list from right to left if you want to sort in descending order
    # i = 8
    # while i >= 0:
    #     count[i] += count[i + 1]
    #     i = i - 1

    # Build the output array by placing elements in sorted order
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output back to the original array
    for i in range(n):
        arr[i] = output[i]

    return arr


def radix_sort(arr):
    """
    Main function to sort `arr` using Radix Sort.
    """
    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Perform counting sort for each digit, starting with the least significant digit
    exp = 1
    while max_val // exp > 0: # this loop runs until all the 3 digits of each number in the list are addressed
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr # final sorted list


nums = [99, 97, 122, 121]

nums = radix_sort(nums)
for i in nums:
    print(chr(i))



# print(chr(99))

# print('Aakash' == 'Aakash')