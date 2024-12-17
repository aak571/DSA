# arr = [6, 1, 80, -56, 12]
# #       0  1  2    3   4

# f()
# mid = len(arr) // 2 # 2.5 = 2
# l = f(arr[:mid]) -> f([6, 1]) -> [1, 6]
# r = f(arr[mid:]) -> f([80, -56, 12]) -> [-56, 12, 80]
# return merge(l, r) -> [-56, -6, 1, 12, 80]




# merge(l, r): l = [1, 90]   r = [-56, 12, 80]
# i = j = 0            i                       j
# sorted_array = []
# while i < len(l) and j < len(r):
#  if l[i] < r[j]:
#      sorted_array.append(l[i]) #
#      i = i + 1
#   else:
#      sorted_array.append(r[j]) # [-56, 1, 12, 80]
#      j = j + 1

# sorted_array.extend(l[i:]) # [-56, 1, 12, 80, 90]
# sorted_array.extend(r[j:]) # null


# Time Compl - O(n*log(n)) - best, avg, worst
# Space Compl - O(n) -> n + n + n + n + n + n -> O(n)

def merge_sort(arr):
    if len(arr) <= 1:  # Base case: a single element is already sorted
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Conquer by merging sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []  # To store the merged sorted array
    i = j = 0  # Pointers for left and right arrays

    # Step 3: Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example usage:
arr = [-6, 1, 80, -56, 12]
print("Original Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)













