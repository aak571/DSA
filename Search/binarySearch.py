# nums = [12, 5, 23, 57, 78, 34, 765]
#Sort the list
# nums = [5, 12, 23, 34, 57, 78, 765]

#Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    #  low + (high - low) // 2
    while low <= high:
        mid = (low + high) // 2  # Calculate mid-point to avoid overflow
        print(mid)
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found


# Example Usage
data = [10, 20, 30, 40, 50, 60, 70]
target_value = 40

result = binary_search(data, target_value)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# print(5 + (1 + 2) // 2)


# Time Complexity
# Best - O(1)
# Avg - O(log(n))
# Worst - O(log(n))

# Space Complexity
# Best, avg, worst -> O(1) -> Iterative opproach
# Best, avg, worst -> O(log(n)) -> Recursive opproach