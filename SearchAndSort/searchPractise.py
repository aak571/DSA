def sort(arr):
    return sorted(arr)  # Timesort -> worst case -> O(n*log(n))

nums = [5, 4, 3, 2, 1]
print(sort(nums))

# Radix Sort -> Sorts it with digits positions -> non-comparison algo
# ['23', '21', '34'] '3' -> 3 int('3') = 3




def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for base 10

    # Count occurrences of each digit at the current position (exp)
    for num in arr:
        index = (int(num) // exp) % 10
        count[index] += 1

    # Update count[i] to store the position of this digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (int(arr[i]) // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the sorted elements back into the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(map(int, arr))

    # Perform counting sort for each digit's place
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage:
unsorted = list(map(int, input().split()))
unsorted = ['32', '434', '232']
radix_sort(unsorted)
print(unsorted)



# def double(num):
#     return 2 * num

# nums = [1, 2, 3, 4]
# print(list(map(double, nums)))

# num = int(input('Enter a number: '))   # by default input() will take in a string
# print(3 * num)

# str = 'Hello everyone- hopeu r - are  -   good    !   !   !'
# l = str.split('-') # -> returns a list
# print(l)

# nums = list(map(int, input().split()))
# print(nums)